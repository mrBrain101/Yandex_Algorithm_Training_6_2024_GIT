def del_median(nums: list[int], n: int) -> list:
    nums.sort()
    res = []
    l, r = 0, n - 1
    while n > 0:
        if n % 2 == 0:
            m1_idx = l + (r - l) // 2
            m2_idx = m1_idx + 1
            if m2_idx > r:
                med_idx = m1_idx
            else:
                med_idx = m1_idx if nums[m1_idx] < nums[m2_idx] else m2_idx
        else:
            med_idx = l + (r - l) // 2
        res.append(nums.pop(med_idx))
        n -= 1
        r -= 1
    return res


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        nums = list(map(int, f.readline().split()))
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, del_median(nums, n))))
