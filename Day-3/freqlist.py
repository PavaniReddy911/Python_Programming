n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

print("Original List:", nums)

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequencies:")
for key, value in freq.items():
    print(key, "->", value)
