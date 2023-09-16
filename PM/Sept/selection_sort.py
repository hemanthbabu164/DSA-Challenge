def selectionSort(arr):
    n =len(arr)
    for i in range(n):
        min_index = i

        # find the index of smallest ele in unsorted portion 
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j     
        # swap the min ele and first ele of unsorted portion
        arr[i],arr[min_index]=arr[min_index],arr[i]

arr=[345,67,23,78,12,55]
selectionSort(arr)
print("Sorted Array: ",arr)

'''
Time complexity: O(n^2) -- obv not efficient for large lists
Space complexity: O(1)
'''