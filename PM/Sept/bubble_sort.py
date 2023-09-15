def bubbleSort(array):
    n=len(array)
    swap=False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                swap=True
                array[j],array[j+1]=array[j+1],array[j]     #making a swap
        if not swap:    #means the array is sorted
            return

arr=[56,78,2,59,3,89]
bubbleSort(arr)
print(arr)


'''
Time Complexity: O(N2) 
Auxiliary Space: O(1)
'''