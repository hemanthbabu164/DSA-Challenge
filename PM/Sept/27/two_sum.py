'''
Write a Python function called two_sum that takes a list of integers nums and 
an integer target as input and returns a list of two integers 
containing the indices of the two numbers from the input list that add up to the target.
You can assume that each input has exactly one solution, and you may not use the same element twice.

Your function should:

1.Return the indices (as a list) of the two numbers in the order they appear in the input list.

2.You can assume that there will be exactly one solution, and you may not use the same element twice
'''

def two_sum(nums, target):
    num_indices = {}  # Dictionary to store number-index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_indices:
            return [num_indices[complement], i]
        
        num_indices[num] = i
    
    return []


print(two_sum([2, 7, 11, 15], 9))  # [0, 1] (2 + 7 = 9)
print(two_sum([3, 2, 4], 6))  # [1, 2] (2 + 4 = 6)
print(two_sum([3, 3], 6))  # [0, 1] (3 + 3 = 6)

'''
Time Complexity: O(N)
Space Complexity: O(N)
'''
