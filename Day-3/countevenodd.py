def count(numbers):
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)


even = []
odd = []

n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

count(nums)

print("Even numbers:", even)
print("Odd numbers:", odd)
