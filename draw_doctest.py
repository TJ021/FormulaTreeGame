>>> draw_formula_tree(build_tree('x'))
'x'
>>> draw_formula_tree(build_tree('-x'))
'- x'
>>> draw_formula_tree(build_tree('(x+y)'))
'+ y\n  x'
>>> draw_formula_tree(build_tree('((x+y)*x)'))
'* x\n  + y\n    x'
>>> draw_formula_tree(build_tree('((x+y)*(x*y))'))
'* * y\n    x\n  + y\n    x'
>>> draw_formula_tree(build_tree('(x*(x*y))'))
'* * y\n    x\n  x'
>>> draw_formula_tree(build_tree('(x*-(x*y))'))
'* - * y\n      x\n  x'
>>> draw_formula_tree(build_tree('(-x*(x*y))'))
'* * y\n    x\n  - x'
>>> draw_formula_tree(build_tree('(-x*((x*y)*(x+y)))'))
'* * + y\n      x\n    * y\n      x\n  - x'
>>> draw_formula_tree(build_tree('(-x*-((x*y)*(x+y)))'))
'* - * + y\n        x\n      * y\n        x\n  - x'