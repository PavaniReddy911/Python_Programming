class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
       
        super().__init__(name, salary)
        
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


Employee1 = Employee("Ravi", 45000)
Employee1.display()

print("---- Manager Details ----")

Manager1 = Manager("Ravi", 45000, "Civil")
Manager1.display()
