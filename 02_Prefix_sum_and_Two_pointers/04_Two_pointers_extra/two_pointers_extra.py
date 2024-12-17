def cnt_seqs(nums, n, k):
    nums.sort()
    days = 0
    cnt = 0
    l = 0
    r = 0    
    while r < n:
        while r < n and nums[r] - nums[l] <= k:
            r += 1
        cnt = r - l
        days = max(days, cnt)
        
        if r == n:
            break
        
        while l < r and nums[l] + k < nums[r]:
            l += 1
    
    return max(days, n - l)

if __name__ == '__main__':
    with open('input.txt') as f:
        n, k = map(int, f.readline().split())
        nums = list(map(int, f.readline().split()))
    with open('output.txt', 'w') as f:
        f.write(str(cnt_seqs(nums, n, k)))