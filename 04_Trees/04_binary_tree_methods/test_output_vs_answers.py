with open('output.txt') as f:
    output = [line.strip() for line in f.readlines()]

with open('answers.txt') as f:
    output2 = [line.strip() for line in f.readlines()]

if output == output2:
    print('YES')
else:
    print('NO')