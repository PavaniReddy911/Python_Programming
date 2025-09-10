
my_list = []

n = int(input("Enter number of elements to add: "))

for i in range(n):
    
    element = input(f"Enter element {i+1}: ")
    if i<0:
        my_list.append(element)

print("Final List:", my_list)


