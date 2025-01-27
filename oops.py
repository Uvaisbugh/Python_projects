#constrectors in python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name, "Salary:", self.salary)

emp1 = Employee("John", 50000)
emp1.display()


# Inheritance in Python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name, "Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project
    def display(self):
        super().display()
        print("Project:", self.project)

emp1 = Employee("John", 50000)  
emp1.display()

mgr1 = Manager("David", 60000, "Product X")

mgr1.display()


# Polymorphism in Python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name, "Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project
    def display(self):
        super().display()
        print("Project:", self.project)

emp1 = Employee("John", 50000)
emp1.display()

mgr1 = Manager("David", 60000, "Product X")
mgr1.display()

employees = [emp1, mgr1]
for emp in employees:
    emp.display()
    
# Encapsulation in Python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def display(self):
        print("Name:", self.__name, "Salary:", self.__salary)

emp1 = Employee("John", 50000)
emp1.display()
print(emp1.__name)


# Composition in Python
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.obj_salary = salary
    def total_salary(self):
        return self.obj_salary.annual_salary()

emp1 = Employee("John", Salary(50000, 10000))
print(emp1.total_salary())

# Aggregation in Python
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.obj_salary = salary
    def total_salary(self):
        return self.obj_salary.annual_salary()
    
# destructors in python
class Employee:
    def __init__(self):
        print("Employee created.")
    def __del__(self):
        print("Destructor called, Employee deleted.")

emp1 = Employee()   
del emp1    