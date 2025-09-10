string = input("Enter a string: ")
ch = input("Enter the character to search: ")

positions = [] 

for i in range(len(string)):
    if string[i] == ch:
        positions.append(i)

if positions:
    print(f"Character '{ch}' found at positions:", positions)
    print(f"Total occurrences: {len(positions)}")
else:
    print(f"Character '{ch}' not found in the string.")

