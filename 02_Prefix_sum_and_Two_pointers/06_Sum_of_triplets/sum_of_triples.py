def sum_of_triplets(nums, n):
    MOD = 10**9 + 7
    prefix_sum = [0] * (n)
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    s1 = [0] * (n)
    for i in range(n):
        s1[i] = prefix_sum[n-1] - prefix_sum[i]

    s2 = [0] * (n)
    for i in range(n-1, -1, -1):
        s2[i] = prefix_sum[i] - nums[i]

    res = 0
    for i in range(n):
        res += nums[i] * s1[i] * s2[i] % MOD
    return res % MOD

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        nums = list(map(int, f.readline().split()))
    with open('output.txt', 'w') as f:
        f.write(str(sum_of_triplets(nums, n)))