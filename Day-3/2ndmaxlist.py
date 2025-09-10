def second_largest(numbers):

    unique_nums = list(set(numbers))
    unique_nums.sort(reverse=True)

    if len(unique_nums) < 2:
        return None 
    return unique_nums[1]

n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))

result = second_largest(nums)

if result is None:
    print("No second largest element found.")
else:
    print("Second largest element is:", result)
