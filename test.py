def find_longest_word(text):
    words = text.split()
    longest = max(words, key=len) if words else ''
    return longest


text = "The quick brown fox jumps over the lazy dog"
print(find_longest_word(text))  # Output: "jumps"


