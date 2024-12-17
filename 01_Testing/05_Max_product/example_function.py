def max_product_pair(nums):
    """
    Find two numbers in the list whose product is maximal.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    tuple: Two numbers in non-decreasing order whose product is maximal.
    """
    min1 = min2 = float('inf')
    max1 = max2 = float('-inf')
    
    for num in nums:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
            
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
            
    if min1 * min2 > max1 * max2:
        return (min1, min2)
    else:
        return (max1, max2)
    
with open('input_tests.txt', 'r') as f:
    lines = f.readlines()

for line in lines[1:]:
    nums = [int(num) for num in line.split()[1:]]
    print(max_product_pair(nums))