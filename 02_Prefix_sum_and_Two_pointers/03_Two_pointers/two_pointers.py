def cntpairs(nums, n, k):
    cnt = 0
    last = 0
    for first in range(n):
        while last < n and nums[last] - nums[first] <= k:
            last += 1
        cnt += n - last
    return cnt

if __name__ == '__main__':
    with open('input.txt') as f:
        n, k = list(map(int, f.readline().split()))
        nums = list(map(int, f.readline().split()))
    with open('output.txt', 'w') as f:
        f.write(str(cntpairs(nums, n, k)))