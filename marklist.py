# Class to manage student details
class StudentDetails:
    def __init__(self, name, roll_no, total_marks):
        """
        Initialize the student with name, roll number, and total marks.
        """
        self.name = name
        self.roll_no = roll_no
        self.total_marks = total_marks

    def display(self):
        """
        Display the student's details along with their grade based on total marks.
        """
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Total Marks: {self.total_marks}")
        
        # Determine grade based on total marks
        if self.total_marks >= 80:
            print("Grade: A")
        elif self.total_marks >= 60:
            print("Grade: B")
        elif self.total_marks >= 40:
            print("Grade: C")
        else:
            print("Grade: F")
    
    def update_marks(self, new_marks):
        """
        Update the student's total marks to a new value.
        """
        self.total_marks = new_marks

    def marklist(self):
        """
        Display the student's name, roll number, and total marks.
        """
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Total Marks: {self.total_marks}")


# Example usage of the class
# Creating an instance for a student named "Faris"
faris = StudentDetails("Faris", 1, 80)
faris.display()  # Display details and grade
faris.update_marks(90)  # Update marks
faris.display()  # Display updated details and grade
faris.marklist()  # Display the marklist

# Creating an instance for a student named "Shamsul"
shamsul = StudentDetails("Shamsul", 2, 70)
shamsul.display()  # Display details and grade
shamsul.update_marks(90)  # Update marks
shamsul.display()  # Display updated details and grade
shamsul.marklist()  # Display the marklist
