
n = int(input("Enter the number: "))

last = n % 10   

while n >= 10:   
    n = n // 10
first = n

print("First digit =", first)
print("Last digit =", last)
print("First+Last is",first+last)