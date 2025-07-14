class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}"
    
class Student(Person):
    def __init__(self, name, age, roll, branch, CGPA):
        super().__init__(name, age)
        self.__roll = roll
        self.__branch = branch
        self.__gpa = CGPA

    def __str__(self):
        return f"Student: {super().__str__()}, Roll: {self.__roll}, Branch: {self.__branch}, CGPA: {self.__gpa}"
    
    @property
    def gpa_update(self):
        return self.__gpa
    @gpa_update.setter
    def gpa_update(self, new_gpa):
        if new_gpa<0 or new_gpa>10:
            raise ValueError("GPA outside bounds: 1-10")
        self.__gpa = new_gpa
    
class Professor(Person):
    def __init__(self, name, age, roll, branch, salary):
        super().__init__(name, age)
        self.__roll = roll
        self.__branch = branch
        self.__salary = salary

    def __str__(self):
        return f"Professor: {super().__str__()}, Roll: {self.__roll}, Branch: {self.__branch}, Salary: {self.__salary}"
    
    @property
    def salary_update(self):
        return self.__salary
    @salary_update.setter
    def salary_update(self, new_salary):
        self.__salary = new_salary

student = Student("Ankit", 20, 101, "CHE", 8.9)
professor = Professor("Raj", 45, 5001, "CHE", 120000)

student.gpa_update = 9.1
professor.salary_update = 130000

print(student)
print(professor)
