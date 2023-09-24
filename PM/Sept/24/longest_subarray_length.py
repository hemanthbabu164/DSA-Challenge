'''
Question: Finding the Longest Subarray with Sum Constraint

You are given an array of positive integers and a target sum 'k'. 
Write a Python function to find the length of the longest subarray 
where the sum of elements in the subarray is less than or equal to 'k'.

'''
def longest_subarray_length(arr, k):
    max_length = 0
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


arr = [1, 2, 3, 4, 5]
k = 11
result = longest_subarray_length(arr, k)
print(result) 

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

