class Student:
    college = "NIT Calicut"

    def __init__(self, name, branch, roll):
        self.name = name
        self.branch = branch
        self.roll = roll

    def show(self):
        print("\nName:", self.name)
        print("Branch:", self.branch)
        print("Roll:", self.roll)
        print("College:", Student.college)

    @classmethod
    def college_switch(cls, clg):
        cls.college = clg
        print("College changed to: ", cls.college)


n = int(input())
student_details = []
for _ in range(n):
    name, roll, branch = input().split()
    student_details.append(Student(name, branch, int(roll)))

for student in student_details:
    student.show()

# College Change
clg = input("\n\nEnter College: ")
Student.college_switch(clg)

print("After college change:")
for student in student_details:
    student.show()