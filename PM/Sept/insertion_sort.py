def insertionSort(array):
    n=len(array)
    if n<=1:
        return
    for i in range(1,n):    #start from second element
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:    #shifting and inserting
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    
arr=[45,67,13,7]
insertionSort(arr)
print(arr)


'''
Time Complexity: O(N2) 
Auxiliary Space: O(1)
'''