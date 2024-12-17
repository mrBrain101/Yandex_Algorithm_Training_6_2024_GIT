def min_valid_seq(n : int, w : str, s : list[str]) -> str:
    if len(s) == n:
        return ''.join(s)
    brackets_map = {'(': ')', ')' : '(', '[': ']', ']': '['}
    open_brackets = set(['(', '['])
    w = {w[i]: i for i in range(len(w))}
    stack = []
    i = 0
    while i < n:
        try:
            if s[i] in open_brackets:
                stack.append(s[i])
                i += 1
            else:
                stack.pop()
                i += 1
        except:
            while len(stack) < n-i:
                if stack:
                    next = list(w)[
                        min(w[brackets_map[stack[-1]]],
                            min(w[list(open_brackets)[0]], 
                                w[list(open_brackets)[1]]))
                                ]
                    if next in open_brackets:
                        s.append(next)
                        stack.append(next)
                        i += 1
                    else:
                        s.append(next)
                        stack.pop()
                        i += 1
                else:
                    next = list(w)[
                        min(w[list(open_brackets)[0]], 
                            w[list(open_brackets)[1]])
                            ]
                    s.append(next)
                    stack.append(next)
                    i += 1
            else:
                while stack:
                    s.append(brackets_map[stack.pop()])
                    i += 1
        finally:
            continue

    return ''.join(s)

if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        w = str(f.readline())
        s = list(map(str, f.readline().strip()))
    with open('output.txt', 'w') as f:
        f.write(min_valid_seq(n, w, s))