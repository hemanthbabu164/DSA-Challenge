def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  
print(are_anagrams("Triangle", "Integral")) 
print(are_anagrams("hello", "world"))  

'''
Time Complexity:  O(N*log(N)) | N=length of longer string
Space Complexity: O(n)
'''
