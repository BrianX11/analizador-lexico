import re

regex_patterns = [
    ('keywords', r'^(if|else|print|exit|ifelse)$'),
    ('single-operators', r'([-+*\\/=()&|;:,<>{}[\\]])'),
    ('multiple-operators', r'(===|!==|[+][+=]|-[-=]|=[=<>]|[<>][=<>]|&&|[|][|])'),
    ('char', r'[a-zA-Z_]\w*'),
    ('num', r'\b\d+(\\.\d*)?([eE][+-]?\d+)?\b'),
    ('white', r'\s+'),
    ('string', r"('(\\\\.|[^'])*'|\"(\\\\.|[^\"])*\")"),
    ('singleline-comment', r'\/\/.*'),
    ('multiline-comment', r'\/[*](.|\n)*?[*]\/')
]

