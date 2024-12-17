def makeprefixsum(nums):
    return [sum(nums[:i]) for i in range(1, len(nums) + 1)]

if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        nums = [int(i) for i in f.readline().split()]
        output = makeprefixsum(nums)
    with open('output.txt', 'w') as f:
        f.write(' '.join(str(i) for i in output))