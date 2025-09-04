num=int(input("Enter Student Number\n"))
name=input("Enter student name\n")
sci=int(input("Enter science marks\n"))
maths=int(input("Enter maths marks\n"))
soc=int(input("Enter social marks\n"))
total=(sci+maths+soc)
avg=(total)/3
print(total)
print(round(avg,2))
print(num,name,total,round(avg,2))
def grade(a):
    if a>40:
        print("Pass")
        if 40<a<50:
            print("C Grade")
        elif 50<a<70:
            print("B Grade")
        elif 70<a<80:
            print("A Grade")
        else:
            print("Distension")
    else:
        print("Fail")

print("Science",grade(sci))
print("Social",grade(soc))
print("Maths",grade(maths))