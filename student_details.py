class Student_details:
    def __init__(self, name, roll_no,total_marks):
        
        self.name = name
        self.roll_no = roll_no
        self.total_marks = total_marks
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Total Marks: {self.total_marks}")
        
        if self.total_marks >= 80:
            print("Grade: A")
        elif self.total_marks >= 60:
            print("Grade: B")
        elif self.total_marks >= 40:
            print("Grade: C")
        else:
            print("Grade: F")
            
    def update_marks(self, new_marks):
        self.total_marks = new_marks
    
    def marklist(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Total Marks: {self.total_marks}")
        
        
faris=Student_details("faris",1,80)
faris.display()
faris.update_marks(90)
faris.display()
faris.marklist()

Shamsul=Student_details("Shamsul",2,70)
Shamsul.display()
Shamsul.update_marks(90)
Shamsul.display()
Shamsul.marklist()