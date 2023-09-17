def partition(array,low,high):
    pivot=array[high]   # choosing a right pivot concerns on the data
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])   # similar to divinding into left and right subarrays
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i+1

def quickSort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quickSort(array,low,pi-1)
        quickSort(array,pi+1,high)


listArray = [3, 6, 8, 10, 1, 2, 19]
quickSort(listArray,0,len(listArray)-1)
print(listArray)


'''
Time Complexity: O(nlogn)
Space Complexity: O(n)

'''
