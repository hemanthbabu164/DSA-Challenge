def find_missing_numbers(nums1, nums2):
    
    num_count = {}
    for num in nums1:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    for num in nums2:
        if num in num_count and num_count[num] > 0:
            num_count[num] -= 1
    missing_numbers = []
    for num, count in num_count.items():
        if count > 0:
            missing_numbers.extend([num] * count)

    return missing_numbers

nums1 = [4, 3, 2, 7, 8, 2, 1]
nums2 = [4, 3, 2, 7, 8, 1]
result = find_missing_numbers(nums1, nums2)
print(result) 

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''