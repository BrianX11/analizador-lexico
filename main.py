import re

regex_patterns = [
    ('keywords', r'/^(if|else|print|exit|ifelse)$/g'),
    ('single-operators', r'/([-+*\/=()&|;:,<>{}[\]])/g'),
    ('multiple-operators', r'/(===|!==|[+][+=]|-[-=]|=[=<>]|[<>][=<>]|&&|[|][|])/g'),
    ('char', r'/[a-zA-Z_]\w*/g'),
    ('num', r'/\b\d+(\.\d*)?([eE][+-]?\d+)?\b/g'),
    ('white', r'/\s+/g'),
    ('string', r"('(\\.|[^'])*'|\"(\\.|[^\"])*\")/g"),
    ('comment', r'/\/\/.*/g'),
    ('multiline-comment', r'/\/[*](.|\n)*?[*]\//g')
]

regex_patterns = [(name, re.compile(pattern)) for name, pattern in regex_patterns]
