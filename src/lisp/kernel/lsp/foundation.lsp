;;(in-package :core)
(eval-when (eval compile load) (core:select-package :core))


(if (boundp 'lambda-list-keywords)
    nil ; don't redefine
    (defconstant lambda-list-keywords
      '(&ALLOW-OTHER-KEYS
        &AUX &BODY &ENVIRONMENT &KEY
        &OPTIONAL &REST
        &VA-REST
        &WHOLE) ))


;; Temporary check-type - everything is true
(fset 'check-type
      #'(lambda (whole env) t)
      t)

(defun 1- (num) (- num 1))
(defun 1+ (num) (+ num 1))



#||
(si::fset 'and
          #'(lambda (whole env)
              (let ((forms (cdr whole)))
                (if (null forms)
                    t
                    (if (null (cdr forms))
                        (car forms)
                        `(if ,(car forms)
                             (and ,@(cdr forms)))))))
          t)


(si::fset 'or
          #'(lambda (whole env)
              (let ((forms (cdr whole)))
                (if (null forms)
                    nil
                    (if ( null (cdr forms))
                        (car forms)
                        (let ((tmp (gensym)))
                          `(let ((,tmp ,(car forms)))
                             (if ,tmp
                                 ,tmp
                                 (or ,@(cdr forms)))))))))
          t )
||#



(defun constantly (object)
  #'(lambda (&rest arguments) object))


(defun simple-program-error (e1 &rest args)
  (apply 'error e1 args))

(defun simple-reader-error (stream e1 &rest args)
  (apply 'error e1 args))


(fset 'return #'(lambda (whole env)
                  (let ((val (cadr whole)))
                    `(return-from nil ,val)))
      t)

#| --- loose this - its in evalmacros where ecl had it |#
#+clasp-min
(si::fset 'psetq #'(lambda (whole env)
                     "Syntax: (psetq {var form}*)
Similar to SETQ, but evaluates all FORMs first, and then assigns each value to
the corresponding VAR.  Returns NIL."
                     (let ((l (cdr whole))
                           (forms nil)
                           (bindings nil))
                       (block nil
                         (tagbody
                          top
                            (if (endp l) (return (list* 'LET* (nreverse bindings) (nreverse (cons nil forms)))))
                            (let ((sym (gensym)))
                              (push (list sym (cadr l)) bindings)
                              (push (list 'setq (car l) sym) forms))
                            (setq l (cddr l))
                            (go top)))))
          t )



(fset 'when #'(lambda (def env)
                `(if ,(cadr def) (progn ,@(cddr def))))
      t)


(fset 'unless #'(lambda (def env)
                  `(if ,(cadr def) nil (progn ,@(cddr def))))
      t)



(defun si::while-until (test body jmp-op)
  (let ((label (gensym))
        (exit (gensym)))
    `(TAGBODY
        (GO ,exit)
      ,label
        ,@body
      ,exit
        (,jmp-op ,test (GO ,label)))))

(fset 'si::while #'(lambda (def env)
                     (si::while-until (cadr def) (cddr def) 'when))
      t)


(fset 'si::until #'(lambda (def env)
                     (si::while-until (cadr def) (cddr def) 'unless))
      t)





(fset 'cons-cdr #'(lambda (def env) `(cdr ,(cadr def))) t)

(eval-when (:compile-toplevel :load-toplevel :execute)
  (select-package :ext))

(core:fset 'checked-value
      #'(lambda (whole env)
          `(the ,@(cdr whole)))
      t)

(eval-when (:compile-toplevel :load-toplevel :execute)
  (core:select-package :core))


(si::fset 'prog1 #'(lambda (whole env)
                     (let ((sym (gensym))
                           (first (cadr whole))
                           (body (cddr whole)))
                       (if body
                           `(let ((,sym ,first))
                              ,@body
                              ,sym)
                           first)))
          t)


(defvar *bytecodes-compiler* nil)



;;
;; TODO: Rewrite this in C++ when you get the chance - a lot of stuff depends on it
;;  "Concatenate LISTS by changing them."

#+(or)(defun nconc (&rest lists)
        (setq lists (do ((p lists (cdr p)))
                        ((or (car p) (null p)) p)))
        (do* ((top (car lists))
              (splice top)
              (here (cdr lists) (cdr here)))
             ((null here) top)
          (rplacd (last splice) (car here))
          (if (car here)
              (setq splice (car here)))))

;;
;;   "Return true if OBJECT is the same as some tail of LIST, otherwise false."
;;
(defun tailp (object list)
  (if (null list)
      (null object)
    (do ((list list (cdr list)))
        ((atom (cdr list)) (or (eql object list) (eql object (cdr list))))
      (if (eql object list)
          (return t)))))
;;
;;   "Return a copy of LIST before the part which is the same as OBJECT."
;;
(defun ldiff (list object)
  (unless (eql list object)
    (do* ((result (list (car list)))
          (splice result)
          (list (cdr list) (cdr list)))
        ((atom list) (if (eql list object) (rplacd splice nil)) result)
      (if (eql list object)
          (return result)
        (setq splice (cdr (rplacd splice (list (car list)))))))))
;; stuff




;; in-package macro is re-defined in evalmacros.lsp
(si::fset 'in-package #'(lambda (whole env)
                          `(eval-when (:compile-toplevel :load-toplevel :execute)
                             (si::select-package ,(string (cadr whole)))
                             *package*))
          t)






(fset 'apply-key #'(lambda (w e)
                     (let ((key (cadr w))
                           (element (caddr w)))
                       `(if ,key
                            (funcall ,key ,element)
                            ,element)))
      t)

;;   "Add ITEM to LIST unless it is already a member."
(defun adjoin (item list &key key (test #'eql) test-not)
  (when test-not
    (setq test (complement test-not)))
  (if (member (apply-key key item) list :key key :test test)
      list
    (cons item list)))




;;
;; This is defined in ecl>>lsp>>load.d
;; It keeps track of the current source location
;; I should use it.
(defparameter *source-location* '("-no-file-" 0 . 0))


;; Required by REGISTER-GLOBAL in cmp/cmpvar.lsp
(si::fset 'pushnew #'(lambda (w e)
                       (let ((item (cadr w))
                             (place (caddr w)))
                         `(setq ,place (adjoin ,item ,place))))
          t)


(defun hash-table-iterator (hash-table)
  (let ((number-of-buckets (hash-table-number-of-hashes hash-table))
        (hash 0))
    (labels ((advance-hash-table-iterator ()
               (declare (core:lambda-name advance-hash-table-iterator))
               #+(or)(core:bformat t "Starting with hash -> %d%N" hash)
               (tagbody
                top
                  (let ((entry (core:hash-table-bucket hash-table hash)))
                    #+(or)(core:bformat t "  entry -> %s%N" entry)
                    (if (and (null entry) (< hash number-of-buckets))
                        (progn
                          #+(or)(core:bformat t "Empty - incrementing hash%N")
                          (incf hash)
                          (if (< hash number-of-buckets)
                              (go top))
                          #+(or)(core:bformat t "a-h-t-i returning NIL%N")
                          (return-from advance-hash-table-iterator nil))
                        (progn
                          #+(or)(core:bformat t "expr was nil entry -> %s%N" entry)
                          (incf hash)
                          (return-from advance-hash-table-iterator entry)))))))
      (function (lambda ()
        (if (>= hash number-of-buckets)
            nil
            (let ((entry (advance-hash-table-iterator)))
              #+(or)(core:bformat t " returned entry -> %s%N" entry)
              (if entry
                  (values t (car entry) (cdr entry))
                  nil))))))))

;   "Substitute data of ALIST for subtrees matching keys of ALIST."
(defun sublis (alist tree &key key (test #'eql) test-not)
  (when test-not
    (setq test (complement test-not)))
  (labels ((sub (subtree)
                (let ((assoc (assoc (apply-key key subtree) alist :test test)))
                  (cond
                   (assoc (cdr assoc))
                   ((atom subtree) subtree)
                   (t (let ((car (sub (car subtree)))
                            (cdr (sub (cdr subtree))))
                        (if (and (eq car (car subtree)) (eq cdr (cdr subtree)))
                            subtree
                          (cons car cdr))))))))
    (sub tree)))
;   "Substitute data of ALIST for subtrees matching keys of ALIST destructively."
(defun nsublis (alist tree &key key (test #'eql) test-not)
  (when test-not
    (setq test (complement test-not)))
  (labels ((sub (subtree)
                (let ((assoc (assoc (apply-key key subtree) alist :test test)))
                  (cond
                   (assoc (cdr assoc))
                   ((atom subtree) subtree)
                   (t
                    (rplaca subtree (sub (car subtree)))
                    (rplacd subtree (sub (cdr subtree)))
                    subtree)))))
    (sub tree)))


(defun invoke-unix-debugger ()
  (gdb "invoking unix debugger"))


(defun signal-type-error (datum expected-type)
  (error 'type-error :datum datum :expected-type expected-type))


(defun inform (fmt &rest args)
  (apply #'bformat t fmt args))

(si::fset 'cons-car #'(lambda (w e)
                        `(car ,(cadr w)))
          t)

(in-package :cl)

;; We do not use this macroexpansion, and thus we do not care whether
;; it is efficiently compiled by ECL or not.
(core:fset 'multiple-value-bind
           #'(lambda (whole env)
               (declare (core:lambda-name multiple-value-bind-macro))
               (let ((vars (cadr whole))
                     (form (caddr whole))
                     (body (cdddr whole))
                     (restvar (gensym)))
                 `(multiple-value-call
                      #'(lambda (&optional ,@(mapcar #'list vars) &rest ,restvar)
                          (declare (ignore ,restvar))
                          ,@body)
                    ,form)))
           t)

(defun warn (x &rest args)
  (core:bformat t "WARN: %s %s%N" x args))


(defun class-name (x)
  (core:name-of-class x))

(defun invoke-debugger (cond)
  (core:invoke-internal-debugger cond))

(export 'class-name)

(in-package :core)

(defun warn-or-ignore (x &rest args)
  nil)
(export 'warn-or-ignore)

