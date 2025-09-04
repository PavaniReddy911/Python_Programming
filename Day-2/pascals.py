n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n-i), end="")   # spaces for alignment
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)   # formula for binomial coefficients
    print()
