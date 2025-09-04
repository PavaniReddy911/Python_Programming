def check_input():
    a = input("Enter a value: ")

    if a.isdigit():
        print("Number")
    elif a.isalpha():
        print("Alphabet")
    else:
        print("Special Character")

check_input()



def check_input():
    a = input("Enter a value: ")

    if '0' <= a <= '9':
        print("Number")
    elif 'a' <= a <= 'z' or 'A' <= a <= 'Z':
        print("Alphabet")
    else:
        print("Special Character")

check_input()
