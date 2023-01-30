import re

regex_patterns = [
    ('keywords', r'^(if|else|print|exit|ifelse)$'),
    ('single-operators', r'([-+*\/=()&|;:,<>{}[\]])'),
    ('multiple-operators', r'(===|!==|[+][+=]|-[-=]|=[=<>]|[<>][=<>]|&&|[|][|])'),
    ('char', r'[a-zA-Z_]\w*'),
    ('num', r'\b\d+(\.\d*)?([eE][+-]?\d+)?\b'),
    ('white', r'\s+'),
    ('string', r"('(\\.|[^'])*'|\"(\\.|[^\"])*\")"),
    ('singleline-comment', r'\/\/.*'),
    ('multiline-comment', r'\/[*](.|\n)*?[*]\/')
]

def get_pattern(tuple_list, type):
    return next(tup for tup in tuple_list if tup[0] == type)[1];

def analyzer(input):
    input = re.sub(get_pattern(regex_patterns, 'singleline-comment'), "", input)
    input = re.sub(get_pattern(regex_patterns, 'multiline-comment'), "", input)

    temp = ""
    _next = ""

    for i in range(len(input)):

        temp += input[i]
        if(i+1!=len(input)):
            _next = input[i+1];
        temp = temp.strip()

        a = re.search(get_pattern(regex_patterns, 'single-operators'), _next)
        b = re.search(get_pattern(regex_patterns, 'white'), _next)
        c = re.search(get_pattern(regex_patterns, 'num'), temp)

        if(re.search(get_pattern(regex_patterns, 'keywords'), temp) and re.search(get_pattern(regex_patterns, 'white'), _next)):
            print("Keyword: %s" % temp)
            temp = ""
        elif(re.search(get_pattern(regex_patterns, 'single-operators'), _next) or re.search(get_pattern(regex_patterns, 'white'), _next) and re.search(get_pattern(regex_patterns, 'char'), temp)):
            print("Id: %s" % temp)
            temp = ""
        elif(re.search(get_pattern(regex_patterns, 'single-operators'), _next) or re.search(get_pattern(regex_patterns, 'multiple-operators'), temp)):
            print("Operator: %s" % temp)
            temp = ""
        elif(re.search(get_pattern(regex_patterns, 'single-operators'), temp)):
            for k in range(len(temp)):
                if re.search(get_pattern(regex_patterns, 'single-operators'), temp[k]):
                    print("Operator: %s" % temp[k])
            temp = ""
        elif temp != "":
            if(re.search(get_pattern(regex_patterns, 'num'), temp)):
                print("Number: %s" % temp)
                temp = ""
            elif((temp[0]=="\"" or temp[0]=="\'") and re.search(get_pattern(regex_patterns, 'string'), temp)):
                print("String: %s" % temp)
                temp = ""

analyzer('if(a==3){ i=a*1 }')
