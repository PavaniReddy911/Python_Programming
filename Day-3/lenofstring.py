def find_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("\nLength of first string:", find_length(str1))
print("Length of second string:", find_length(str2))


if str1 == str2:
    print("\nBoth strings are equal.")
elif str1 > str2:
    print("\nFirst string is greater than second string.")
else:
    print("\nSecond string is greater than first string.")

concat = str1 + str2
print("\nConcatenated string:", concat)
