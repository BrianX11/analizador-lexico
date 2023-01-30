regex_patterns = [
    ('keywords', '/^(if|else|print|exit|ifelse)$/g'),
    ('single-operators', '/([+-*/=()&|;:,<>{}[\]])/g'),
    ('multiple-operators', '/(===|!==|[+][+=]|-[-=]|=[=<>]|[<>][=<>]|&&|[|][|])/g)'),
    ('char', '/[a-zA-Z_]\w*/g'),
    ('num', '/\b\d+(\.\d*)?([eE][+-]?\d+)?\b/g'),
    ('white', '/\s+/g'),
    ('string',"""/('(\\.|[^'])*'|"(\\.|[^"])*")/g')""")
    ('comment', '/\/\/.*/g'),
    ('multiline-comment','/\/[*](.|\n)*?[*]\//g')
]


