# Find the kth smallest number in a list using Quick Select Algorithm

def find_kth_smallest(nums, k):
    if k < 1 or k > len(nums):
        return "Invalid input"

    # Use Quickselect algorithm to find the kth smallest element
    def quickselect(nums, left, right, k):
        if left == right:
            return nums[left]

        pivot_index = partition(nums, left, right)
        
        if k == pivot_index:
            return nums[pivot_index]
        elif k < pivot_index:
            return quickselect(nums, left, pivot_index - 1, k)
        else:
            return quickselect(nums, pivot_index + 1, right, k)

    def partition(nums, left, right):
        pivot = nums[right]
        i = left - 1

        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    return quickselect(nums, 0, len(nums) - 1, k - 1)


result = find_kth_smallest([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 3)
print(result)  

'''
Time complexity : Average- O(n) | Worst - O(n^2)
Space complexity : O(1)

'''