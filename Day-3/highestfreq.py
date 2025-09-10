def highest_frequency_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

s = input("Enter a string: ")
char, count = highest_frequency_char(s)
print("Highest frequency character:", char, "with count", count)
