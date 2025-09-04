import math
n = int(input("Enter a number: "))

print(f"Strong numbers between 1 and {n} are:")

for num in range(1, n+1):
    sum_fact = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_fact += math.factorial(digit)
        temp //= 10

    if sum_fact == num:
        print(num, end=" ")

