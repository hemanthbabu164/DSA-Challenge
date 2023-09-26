def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)

    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]

    return shortest_str


print(longest_common_prefix(["flower", "flour", "flourish"]))  
print(longest_common_prefix(["dog", "car", "racecar"]))  
print(longest_common_prefix(["apple", "appetizer", "april"]))  

'''
Time Complexity: O(N*log(N) + M), where N is the number of strings and M is the length of the common prefix
Space Complexity:  O(M), where M is the length of the common prefix

'''
