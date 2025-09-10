vowels_list = ['a', 'e', 'i', 'o', 'u']

def count_characters(s):
    vowels = consonants = 0
    
    for ch in s.lower():  
        if ch.isalpha():  
            if ch in vowels_list:
                vowels += 1
            else:
                consonants += 1
    
    print("Vowels:", vowels)   
    print("Consonants:", consonants)

text = input("Enter a string: ")
count_characters(text)

