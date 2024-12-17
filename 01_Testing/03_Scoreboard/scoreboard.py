def read_scoreboard(input) -> str:
    lines = [l for l in input.splitlines()]
    n = int(lines[0])
    lines = lines[1:]

    # check if turned off or one on
    check_empty = ''.join(lines)
    if '#' not in check_empty:
        return 'X'

    def catch_random_patterns(lines):
        '''catch random patterns'''
        seen_hash = False
        seen_dot = False
        for i, line in enumerate(lines):
            if '#' in line:
                seen_hash = True
            elif seen_hash and line.replace('.', '') == '':
                seen_dot = True
            if '#' in line and seen_hash and seen_dot:
                return 'X'

    def remove_dot_strings(lines)->list[str]:
        '''remove full dot strings'''
        return [s for s in lines if not s.strip('.') == '']

    def transpose(lines)->list[str]:
        '''transpose scoreboard'''
        return [''.join(row) for row in zip(*lines)]
    
    # remove horizontal and vertical full dot strings with checks for 
    # random patterns
    if catch_random_patterns(lines) == 'X': return 'X'
    lines = remove_dot_strings(lines)
    lines = transpose(lines)
    if catch_random_patterns(lines) == 'X': return 'X'
    lines = remove_dot_strings(lines)
    lines = transpose(lines)

    # check if left column is all hashes:
    if any([line[0] != '#' for line in lines]):
        return 'X'

    # check if I
    i = 0
    for l in lines:
        if l.strip('#') == '':
            continue
        else:
            i += 1
    if i == 0:
        return 'I'

    # check if O or C
    # if _ number of first and last lines are # and _ number of middle lines
    #  contain . of the same length then O or C
    if lines[0].replace('#', '') == '' and lines[-1].replace('#', '') == '':
        dot_len = []
        h = 0
        seen_hash = False
        seen_dot = False
        for i, l in enumerate(lines):
            r = l.replace('#', '')
            if r == '':
                seen_hash = True
            elif r != '':
                dot_len.append(len(r))
                seen_dot = True
                if l[-1] == '#':
                    h += 1
            if seen_hash and seen_dot and r == '':
                if any(l.replace('#', '') != '' for l in lines[i+1:]):
                    return 'X'
        if all(x == dot_len[0] for x in dot_len) and h == len(dot_len):
            return 'O'
        elif all(x == dot_len[0] for x in dot_len):
            return 'C'
        else:
            return 'X'
        
    # check if L
    if lines[0].replace('#', '') != '' and lines[-1].replace('#', '') == '':
        dot_len = []
        h = 0
        for l in lines[0:-1]:
            r = l.replace('#', '')
            if r != '':           
                if '#' in l.lstrip('#'):
                    return 'X'
                dot_len.append(len(r))
        if all(x == dot_len[0] for x in dot_len):
            return 'L'
        
    # check if P
    if lines[0].replace('#', '') == '' and lines[-1][0] == '#':
        dot_len = []
        width_checker = []
        seen_hash = False
        seen_dot = False
        # count dots inside of P circle
        for i, l in enumerate(lines):
            r = l.replace('#', '')
            if r == '':
                seen_hash = True
            elif r != '':
                seen_dot = True
                dot_len.append(len(r))
                width = l.rstrip('#').count('#')
                width_checker.append(width)
            if seen_hash and seen_dot and r == '':
                if any('#' in l.lstrip('#') for l in lines[i+1:]):
                    return 'X'
                else:
                    continue
        if any(x != width_checker[0] for x in width_checker):
            return 'X'
            
        if len(set(dot_len)) == 2 or len(set(dot_len)) == 1:
            return 'P'
        else:
            return 'X'

    # # check if H
    lines_T = transpose(lines)
    if lines_T[0].replace('#', '') == '' and lines_T[-1].replace('#', '') == '':
        middle = []
        for l in lines_T:
            if l.replace('#', '') != '':
                middle.append(l)
        if len(set(middle)) == 1:
            return 'H'
        else:
            return 'X'

    else:
        return 'X'

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.read()

    with open("output.txt", "w") as file:
        file.write(f'{read_scoreboard(input)}')