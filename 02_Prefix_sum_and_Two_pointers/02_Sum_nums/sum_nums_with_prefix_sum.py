def cntsumofk(nums, k):
    count = 0
    prefix_sum_count = {0: 1}
    cumsum = 0

    for num in nums:
        cumsum += num

        if (cumsum - k) in prefix_sum_count:
            count += prefix_sum_count[cumsum - k]
        
        if cumsum in prefix_sum_count:
            prefix_sum_count[cumsum] += 1
        else:
            prefix_sum_count[cumsum] = 1
        
    return count

if __name__ == '__main__':
    with open('input.txt') as f:
        _, k = (int(s) for s in f.readline().split())
        nums = [int(i) for i in f.readline().split()]
        output = cntsumofk(nums, k)
    with open('output.txt', 'w') as f:
        f.write(str(output))