def count_characters(s):
    alphabets = digits = special = 0
    
    for ch in s:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1
    
    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Special characters:", special)

text = input("Enter a string: ")
count_characters(text)


