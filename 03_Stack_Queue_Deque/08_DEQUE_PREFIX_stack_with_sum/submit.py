from collections import deque

class StackWithSum(object):
    def __init__(self):
        self.stack = deque()
        self.sum = deque()
        self.sum.append(0)

    def push(self, x):
        self.stack.appendleft(x)
        self.sum.appendleft(self.sum[0] + x)

    def pop(self):
        x = self.stack.popleft()
        self.sum.popleft()
        return x

    def get_sum(self, k):#yeah
        return self.sum[0] - self.sum[k]
    

stack_w_s = StackWithSum()
with open('input.txt') as f:
    n = int(f.readline())
    for i in range(n):
        line = f.readline()
        if line[0] == '+':
            stack_w_s.push(int(line[1:]))
        elif line[0] == '-':
            print(stack_w_s.pop())
        else:
            print(stack_w_s.get_sum(int(line[1:])))