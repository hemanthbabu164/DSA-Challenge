'''
Write a Python function called has_unique_characters that takes a string as input 
and returns True if all the characters in the string are unique (no character repeats), 
and False otherwise
'''
def has_unique_characters(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True


print(has_unique_characters("abcdefg")) 
print(has_unique_characters("hello"))  
print(has_unique_characters(""))  

'''
Time Complexity: O(N), where N is the length of the input string
Space Complexity: O(C), where C is the number of unique characters in the input string

'''
