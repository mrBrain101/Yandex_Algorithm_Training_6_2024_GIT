from collections import deque

def time_line(n : int, b : int, p : list[int]) -> int:    
    line = deque()
    overflow_stack = []
    time = 0

    for i in range(n):
        if overflow_stack:
            line.appendleft(p[i] + overflow_stack.pop())
        else:
            line.appendleft(p[i])
        if line[-1] <= b:
            time += line[-1]
            line.pop()
        else:
            time += line[-1]
            overflow_stack.append(line.pop() - b)
    else:
        if overflow_stack:
            time += overflow_stack.pop()

    return time

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n, b = map(int, f.readline().split())
        p = list(map(int, f.readline().split()))
    with open('output.txt', 'w') as f:
        f.write(str(time_line(n, b, p)))