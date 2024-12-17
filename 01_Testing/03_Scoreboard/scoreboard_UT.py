def run_tests(f: callable):
    with open('input_tests.txt', "r") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        n = int(lines[i])
        lines_to_pass = lines[i:i+n+1]
        with open('input.txt', 'w') as file: 
            file.writelines(''.join(lines_to_pass))
        with open('input.txt', 'r') as file:
            input = file.read()
            print(''.join(lines_to_pass), end='')
            print(f(input), '\n')
        i += n + 1