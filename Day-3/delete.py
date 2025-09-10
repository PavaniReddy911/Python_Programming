n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

print("Original List:", nums)

pos = int(input("Enter position to delete (starting from 1): "))

if 1 <= pos <= len(nums):
    nums.pop(pos - 1)  
    print("List after deletion:", nums)
else:
    print("Invalid position!")