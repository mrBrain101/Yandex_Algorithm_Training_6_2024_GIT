def bracket_stack(s : str) -> str:
    
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    open_brackets = set(['(', '[', '{'])
    
    for c in s:
        if c in open_brackets:
            stack.append(c)
        elif c in bracket_map:
            if stack == [] or bracket_map[c] != stack.pop():
                return 'no'
    return 'yes' if stack == [] else 'no'

if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline().strip()
    with open('output.txt', 'w') as f:
        f.write(bracket_stack(line))