def word_frequency(text):
    # Split the text into words, remove punctuation, and convert to lowercase
    words = text.split()
    words = [word.strip(".,!?()[]{}:;\"'").lower() for word in words]

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


text = "Sastra is a Deemed University. Sastra is a World class university"
result = word_frequency(text)
print(result)

'''
Time Complexity: O(n)
Space Complexity: O(m) | m=no.of unique words

'''
