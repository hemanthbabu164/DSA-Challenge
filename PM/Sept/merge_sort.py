def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2       # find middle index

        left_half =arr[:mid]    
        right_half=arr[mid:]

        # recursively sort right and left halves
        mergeSort(left_half)
        mergeSort(right_half)

        i=j=k=0

        # merging the sorted halves
        while i<len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                arr[k]=left_half[i]
                i +=1
            else:
                arr[k]=right_half[j]
                j +=1
            k +=1

        # for any leftover elements
        while i<len(left_half):
            arr[k]=left_half[i]
            i +=1
            k +=1
        
        while j<len(right_half):
            arr[k]=right_half[j]
            j +=1
            k +=1


arr=[435,23,56,4,342,67]
mergeSort(arr)
print("Sorted array: ",arr)



'''
Time complexity : O(nlogn) -- in all cases
Space complexity: O(n)
'''