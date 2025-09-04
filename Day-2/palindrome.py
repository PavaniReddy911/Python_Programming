n = int(input("Enter a number: "))

print(f"Palindrome numbers between 1 and {n} are:")

for num in range(1, n+1):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")

n=int(input("Enter a number: "))
print(f"Palindrome numbers between 1 and {n} are:")
for num in range(1,n+1):
    if str(num)==str(num)[::-1]:
        print(num,end=" ")
