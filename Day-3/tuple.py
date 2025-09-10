students = []
for i in range(5):
    roll = int(input("Enter roll.no:"))
    name=input("Enter name:")
    marks=int(input("Enter marks:"))
    students.append((roll,name,marks))
print("Data")
for s in students:
    print(s)


highest = max(students, key=lambda x: x[2])
print("\nStudent with highest marks:", highest[1], "(", highest[2], "marks )")

print("\nStudents who scored more than 75 marks:")
for s in students:
    if s[2] > 75:
        print(s[1], "-", s[2], "marks")
