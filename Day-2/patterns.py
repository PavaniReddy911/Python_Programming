for i in range(1,5+1):
    for j in range(1,5+1):
        print("*",end=" ")
    print()

for i in range(1,5+1):
    for j in range(1,5+1):
        if i==j:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()


for i in range(1,5+1):
    for j in range(1,5+1):
        if i==j:
            print("$",end=" ")
        elif i+j==6:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()