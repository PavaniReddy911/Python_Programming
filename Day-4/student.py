class Student:
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

student1 = Student()
student1.name = "Alice"
student1.roll_no = 101
student1.marks = 89

student2 = Student()
student2.name = "Bob"
student2.roll_no = 102
student2.marks = 95

student1.display()
student2.display()

print("                          ")
print("                          ")
print("-----With Constructor-----")
print("                          ")
print("                          ")

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

student1 = Student("Alice", 101, 89)
student2 = Student("Bob", 102, 95)

student1.display()
student2.display()

