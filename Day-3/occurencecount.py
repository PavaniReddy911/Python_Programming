# Program: Count frequency of characters in a string

def encode(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    encoded = ""
    for ch, count in freq.items():
        encoded += ch + str(count)
    
    return encoded

string = input("Enter a string: ")
print("Encoded string:", encode(string))
