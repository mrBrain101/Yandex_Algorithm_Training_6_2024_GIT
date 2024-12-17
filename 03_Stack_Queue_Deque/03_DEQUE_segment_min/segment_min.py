from collections import deque

def segment_min(nums : list[int], n : int, k : int) -> list[int]:
    dq = deque()

    # analyze first k elements
    for i in range(k):
        while dq and nums[i] < nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    # analyze the rest of the elements
    for i in range(k, n):
        print(nums[dq[0]]) # print the min of the previous window
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[i] < nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    print(nums[dq[0]]) # print the min of the last window

if __name__ == "__main__":
    with open("input.txt") as f:
        n, k = map(int, f.readline().split())
        nums = list(map(int, f.readline().split()))
    segment_min(nums, n, k)