def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Calculate middle index
        if array[mid] == target:
            return mid  # Index if element found
        elif array[mid] < target:
            left = mid + 1  # Right half
        else:
            right = mid - 1  # Left half
    return -1

arr = [67, 5, 23, 98, 45, 32]
arr.sort()
x = int(input("Enter the number to search: "))  # Convert input to integer
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



'''
Time Complexity: O(log n)

Auxiliary Space: O(1)

'''
