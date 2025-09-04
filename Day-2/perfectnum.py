import math
n = int(input("Enter a number: "))
print(f"The perfect numbers between 1 and {n} are:\n")

for num in range(1,n+1):
    sum_div=0
    for i in range(1,num):
        if num%i==0:
            sum_div+=i
    if sum_div==num:
        print(num,end=" ")
