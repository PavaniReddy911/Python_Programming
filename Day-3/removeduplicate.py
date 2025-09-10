n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

print("Original List:", nums)

unique = list(set(nums))

print("List after removing duplicates:", unique)

