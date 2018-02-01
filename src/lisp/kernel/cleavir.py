cleavir_parts = [
    "src/lisp/kernel/contrib/Acclimation/packages",
    "src/lisp/kernel/contrib/Acclimation/locale",
    "src/lisp/kernel/contrib/Acclimation/date",
    "src/lisp/kernel/contrib/Acclimation/language",
    "src/lisp/kernel/contrib/Acclimation/language-english",
    "src/lisp/kernel/contrib/Acclimation/language-french",
    "src/lisp/kernel/contrib/Acclimation/language-swedish",
    "src/lisp/kernel/contrib/Acclimation/language-vietnamese",
    "src/lisp/kernel/contrib/Acclimation/language-japanese",
    "src/lisp/kernel/contrib/Acclimation/condition",
    "src/lisp/kernel/contrib/Acclimation/documentation",
    "src/lisp/kernel/contrib/Acclimation/init",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/packages",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/generic-functions",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/cst",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/cons-cst",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/listify",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/cstify",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/cst-from-expression",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/reconstruct",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/declarations",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/body",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/list-structure",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/bindings",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/conditions",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/client",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/ensure-proper",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/grammar-symbols",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/lambda-list-keywords",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/grammar",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/standard-grammars",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/earley-item",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/earley-state",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/parser",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/scanner-action",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/earley",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Lambda-list/parse-top-levels",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/condition-reporters-english",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/argcount",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/form",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/list-structure",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/declarations",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/lambda-lists",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Code-utilities/destructuring",
    "src/lisp/kernel/contrib/sicl/Code/Readtable/packages",
    "src/lisp/kernel/contrib/sicl/Code/Readtable/generic-functions",
    "src/lisp/kernel/contrib/sicl/Code/Readtable/Simple/packages",
    "src/lisp/kernel/contrib/sicl/Code/Readtable/Simple/readtable",
    "src/lisp/kernel/contrib/sicl/Code/Readtable/Simple/methods",
    "src/lisp/kernel/contrib/closer-mop/closer-mop-packages",
    "src/lisp/kernel/contrib/closer-mop/closer-mop-shared",
    "src/lisp/kernel/contrib/closer-mop/closer-clasp",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/packages",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/more-variables",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/additional-conditions",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/utilities",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/tokens",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/read-common",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/read",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/macro-functions",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/init",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/quasiquote-macro",
    "src/lisp/kernel/contrib/sicl/Code/Reader/Simple/fixup",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Input-output/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Input-output/io",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Meter/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Meter/meter",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/general-purpose-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/fixnum-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/simple-float-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/cons-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/standard-object-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/array-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/scope-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/graphviz-drawing",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Abstract-syntax-tree/map-ast",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-transformations/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-transformations/clone",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-transformations/replace",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-transformations/hoist-load-time-value",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Primop/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/condition-reporters-english",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/query",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/augmentation-functions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/default-augmentation-classes",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/compile-time",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/optimize-qualities",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/declarations",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/type-information",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/default-info-methods",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Environment/eval",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/condition-reporters-english",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/policy",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/define-policy",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/optimize",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Compilation-policy/compute",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/condition-reporters-english",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/source-tracking",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/destructuring",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/check-special-form-syntax",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/environment-query",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/utilities",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/minimal-compilation",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/generate-ast",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/convert-form",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/convert-special",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/convert-primop",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Generate-AST/ast-from-file",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/generic-functions",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/required-parameters",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/optional-parameters",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/rest-parameters",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/key-parameters",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/aux-parameters",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/lambda-list",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/parse-macro",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree/Destructuring/db-defmacro",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/environment-augmentation",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/environment-query",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/variables",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/generic-functions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-function-reference",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-special-binding",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/utilities",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/set-or-bind-variable",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/process-progn",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-sequence",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-variable",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/process-init-parameter",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/itemize-declaration-specifiers",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/itemize-lambda-list",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-setq",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-let-and-letstar",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-code",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-lambda-call",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-constant",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-special",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-primop",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/convert-cst",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/cst-to-ast",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/CST-to-AST/condition-reporters-english",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/datum",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/instruction",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/graph-modifications",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/instruction-mixin-classes",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/graphviz-drawing",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/map-instructions-arbitrary-order",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/set-predecessors",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/map-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/data",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/side-effect-mixins",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/general-purpose-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/box-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/fixnum-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/simple-float-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/cons-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/standard-object-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/array-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/multiple-value-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/environment-related-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR/graphviz-drawing",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/context",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/condition-reporters-english",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/compile-general-purpose-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/compile-fixnum-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/compile-simple-float-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/compile-cons-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/compile-standard-object-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/AST-to-HIR/compile-array-related-asts",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/pool",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/kildall",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/dictionary",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/work-list",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/map-pool",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/iterate",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/initial-work",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/alist-pool",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/bitset",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/interfunction",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/graphviz-drawing",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Liveness/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Liveness/sset",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Liveness/liveness",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Liveness/extend",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/Descriptors/lattice-descriptor",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/Descriptors/values-descriptor",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/Descriptors/function-descriptor",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/Descriptors/unboxed-descriptor",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/Descriptors/eql-descriptor",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/Descriptors/descriptor",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/specialization",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/transfer",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/prune",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/insert-type-checks",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Type-inference/interface",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Escape/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Escape/specialization",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Escape/indicator",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Escape/transfer",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Kildall/Specializations/Escape/interface",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/constant-load-time-value",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/traverse",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/convert-constant-to-immediate",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/hoist-load-time-values",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/compute-ownership",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/inline-calls",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/static-few-assignments",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/type-inference",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/eliminate-load-time-value-inputs",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/coalesce-load-time-values",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/eliminate-typeq",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/simplify-box-unbox",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/function-tree",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/segregate-lexicals",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/eliminate-superfluous-temporaries",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/hir-transformations",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/Remove-useless-instructions/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/Remove-useless-instructions/meter",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/HIR-transformations/Remove-useless-instructions/remove-useless-instructions",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/MIR/general",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/MIR/graphviz-drawing",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Intermediate-representation/HIR-to-MIR/general",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Utilities/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Utilities/utilities",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Basic-blocks/packages",
    "src/lisp/kernel/contrib/sicl/Code/Cleavir/Basic-blocks/basic-blocks",
    "src/lisp/kernel/contrib/sicl/Code/Types/Additional/packages",
    "src/lisp/kernel/contrib/sicl/Code/Types/Additional/types",
    "src/lisp/kernel/contrib/sicl/Code/Conditions/Additional/packages",
    "src/lisp/kernel/contrib/sicl/Code/Conditions/Additional/conditions",
    "src/lisp/kernel/contrib/sicl/Code/Conditions/Additional/condition-reporters-en",
    "src/lisp/kernel/cleavir/packages",
    "src/lisp/kernel/cleavir/cleavir-fixups-and-hacks",
    "src/lisp/kernel/cleavir/system",
    "src/lisp/kernel/cleavir/policy",
    "src/lisp/kernel/cleavir/reader",
    "src/lisp/kernel/cleavir/ast",
    "src/lisp/kernel/cleavir/convert-form",
    "src/lisp/kernel/cleavir/convert-special",
    "src/lisp/kernel/cleavir/eliminate-ltvs",
    "src/lisp/kernel/cleavir/hir",
    "src/lisp/kernel/cleavir/introduce-invoke",
    "src/lisp/kernel/cleavir/toplevel",
    "src/lisp/kernel/cleavir/setup",
    "src/lisp/kernel/cleavir/ast-to-hir",
    "src/lisp/kernel/cleavir/mir",
    "src/lisp/kernel/cleavir/hir-to-mir",
    "src/lisp/kernel/cleavir/ir",
    "src/lisp/kernel/cleavir/gml-drawing",
    "src/lisp/kernel/cleavir/landing-pad",
    "src/lisp/kernel/cleavir/closure-optimize",
    "src/lisp/kernel/cleavir/translate",
    "src/lisp/kernel/cleavir/inline-prep",
    "src/lisp/kernel/cleavir/auto-compile",
    "src/lisp/kernel/cleavir/inline"
]
