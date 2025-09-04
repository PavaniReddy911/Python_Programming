num = int(input("Enter the consumer number: "))
name = input("Enter the consumer name: ")
pmr = int(input("Enter present meter reading: "))
lmr = int(input("Enter last meter reading: "))

tu = pmr - lmr
bill = 0

if tu <= 50:
    bill = tu * 3.80
elif tu <= 100:
    bill = (50 * 3.80) + (tu - 50) * 4.20
elif tu <= 200:
    bill = (50 * 3.80) + (50 * 4.20) + (tu - 100) * 5.10
elif tu <= 300:
    bill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (tu - 200) * 6.30
else:
    bill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (100 * 6.30) + (tu - 300) * 7.50

print(num, name, pmr, lmr, tu, round(bill, 2))
print(f"Hi {name}, your current bill is ₹{round(bill, 2)}")
