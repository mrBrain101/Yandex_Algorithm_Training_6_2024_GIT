def nearest_smaller_right(nums : list[int], n : int) -> list[int]:
    stack = []
    idx = [-1] * n

    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx[stack.pop()] = i
        
        stack.append(i)

    return idx

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        nums = list(map(int, f.readline().split()))
    with open('output.txt', 'w') as f:
        f.write(' '.join(map(str, nearest_smaller_right(nums, len(nums)))))