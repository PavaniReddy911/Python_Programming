def count_words(s):
    words = s.split()
    print("Total number of words:", len(words))

text = input("Enter a string: ")
count_words(text)
