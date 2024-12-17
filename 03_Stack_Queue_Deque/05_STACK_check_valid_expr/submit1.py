import re

def calculate_valid_expr(expr : str) -> str:

    def first_check(expr : str) -> str:
        pattern_spaces_num = r'(\d+)(\s+)(\d+)'
        pattern_spaces_br = r'(\()(\s+)(\))'
        pattern_conseq_operators = r'(\+|\-|\*|\/){2,}'
        pattern_eof_operator = r'(\+|\-|\*|\/)\Z'
        pattern_empty_brackets = r'\(\)'
        pattern_any_extra_char = r'[^\d\s\+\-\*\/()]'
        pattern_first_char = r'(\()(\+|\*|\/)'
        if re.search(pattern_spaces_num, expr) or\
            re.search(pattern_spaces_br, expr) or\
            re.search(pattern_conseq_operators, expr) or\
            re.search(pattern_eof_operator, expr) or\
            re.search(pattern_empty_brackets, expr) or\
            re.search(pattern_any_extra_char, expr) or\
            re.search(pattern_first_char, expr):
            return 'WRONG'
        else:
            expr = expr.replace(' ', '')
            return expr

    def check_brackets(expr : str) -> str:
        expr_br = str(list(c for c in expr if c in ['(', ')']))
        stack = []
        bracket_map = {')': '('}
        
        for c in expr_br:
            if c == '(':
                stack.append(c)
            elif c in bracket_map:
                if stack == [] or bracket_map[c] != stack.pop():
                    return 'WRONG'
                
        return 'fine' if stack == [] else 'WRONG'

    def to_postfix(expr : str) -> str:
        j = 0
        unary_minus = 0
        for j in range(1, len(expr)):
            if expr[j] == '-' and expr[j-1] == '(':
                unary_minus += 1

        stack = []
        postfix = []
        i = 0
        num = ''
        while i < (len(expr) + unary_minus):
            if expr[i].isnumeric():
                while i < len(expr) and expr[i].isnumeric():
                    num += expr[i]
                    i += 1
                else:
                    if i == len(expr):
                        postfix.append(num)
                        break
                postfix.append(num)
                num = ''
            elif expr[i] == '(':
                stack.append(expr[i])
                i += 1
            elif expr[i] == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
                i += 1
            elif i == 0 and expr[i] == '-':
                postfix.append('0')
                stack.append(expr[i])
                i += 1
            elif i > 0 and\
                 expr[i - 1] == '(' and\
                 expr[i] == '-':
                    postfix.append('0')
                    stack.append(expr[i])
                    i += 1
            else:
                if expr[i] in ['+', '-']:
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                stack.append(expr[i])
                i += 1
        while stack:
            postfix.append(stack.pop())

        return postfix

    def calculate_postfix(expr : list[str]) -> int:
        stack = []
        for c in expr:
            if c.isnumeric():
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
                elif c == '*':
                    stack.append(a * b)
                elif c == '/':
                    stack.append(a / b)
        return stack[0]


    if expr.replace(' ', '') == '': return 'WRONG'
    expr = first_check(expr)
    if expr == 'WRONG': return 'WRONG'
    if check_brackets(expr) == 'WRONG': return 'WRONG'
    
    return calculate_postfix(to_postfix(expr))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        expr = f.readline().strip('\n')
    with open('output.txt', 'w') as f:
        f.write(str(calculate_valid_expr(expr)))