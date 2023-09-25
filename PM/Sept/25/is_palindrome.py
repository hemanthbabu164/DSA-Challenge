import re
def is_palindrome(s):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("racecar")) 
print(is_palindrome("A man, a plan, a canal, Panama")) 
print(is_palindrome("hello"))  

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''