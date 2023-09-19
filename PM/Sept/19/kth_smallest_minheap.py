# Find the kth smallest number in a list using min-heap algorithm

import heapq

def find_kth_smallest(nums, k):
    if k < 1 or k > len(nums):
        return "Invalid input"

    # Create a Max-Heap (negate the numbers) and push the first k elements into it
    max_heap = [-num for num in nums[:k]]
    heapq.heapify(max_heap)

    # Push the rest of the elements into the Max-Heap while maintaining its size as k
    for num in nums[k:]:
        if num < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

    # The smallest k elements will be in the Max-Heap, and the kth smallest element is the negation of the root
    return -max_heap[0]


result = find_kth_smallest([3, 0, 4, 5, 9, 2, 6, 5, 3], 5)
print(result)  

'''
Time complexity : O(n * log(k))
Space complexity : O(k)

'''
