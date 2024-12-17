def polish_modesty(expr : list[str]) -> int:
    stack = []
    for c in expr:
        try:
            stack.append(int(c))
        except:
            b = stack.pop()
            a = stack.pop()
            if c == '+':
                stack.append(a+b)
            elif c == '*':
                stack.append(a*b)
            elif c== '-':
                stack.append(a-b)

    return stack[0]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        expr = f.readline().split()
    with open('output.txt', 'w') as f:
        f.write(str(polish_modesty(expr)))