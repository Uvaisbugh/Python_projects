

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Course:
    def __init__(self, name, instrector, price):
        self.name = name
        self.instrector = instrector
        self.price = price
        self.students = []
        
    def enroll(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.name}")
        print()
        
    def get_students(self):
        return self.students
    
    def course_details(self):
        print(f"Course Name: {self.name}")
        print(f"Instrector: {self.instrector}")
        print(f"Price: {self.price}")
        print(f"Students: {', '.join(student.name for student in self.students)}")
        print()
        
    def completed_course(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} completed {self.name}")
        else:
            print(f"{student.name} is not enrolled in {self.name}")
        
        print()
        self.course_details()
            

reproductive_health = Course("Reproductive Health", "Dr. John", 100)
reproductive_health.course_details()

student1 = Student("Alice", 20)
student2 = Student("Bob", 21)
student3 = Student("Charlie", 22)

reproductive_health.enroll(student1)
reproductive_health.enroll(student2)
reproductive_health.enroll(student3)

reproductive_health.course_details()

reproductive_health.completed_course(student1)
reproductive_health.course_details()
        