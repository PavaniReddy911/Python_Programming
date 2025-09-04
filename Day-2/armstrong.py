n = int(input("Enter a number: "))

print(f"Armstrong numbers between 1 and {n} are:")

for num in range(1, n+1):
    num_digits = len(str(num))
    sum_of_powers = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10

    if num == sum_of_powers:
        print(num, end=" ")