# Esercizi:
# Creare una classe Person , estenderla con due sottoclassi Dipendente e Studente
# Estendere Dipendenti con 2 sottoclassi Docente e Freelance
# Una classe deve essere astratta e ogni classe deve avere delle proprietà specializzanti

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname 
    @abstractmethod
    def get_info(self) -> str:
        return f"Name: {self.name}, Surname: {self.surname}"

class Student(Person):
    def __init__(self, name, surname, student_id):
        super().__init__(name, surname)
        self.student_id = student_id 
    def get_info(self) -> str:
        return f"{super().get_info()}, Student ID: {self.student_id}"

class Employee(Person):
    def __init__(self, name, surname, employee_id):
        super().__init__(name, surname)
        self.employee_id = employee_id 
    def get_info(self) -> str:
        return f"{super().get_info()}, Employee ID: {self.employee_id}"

class Teacher(Employee):
    def __init__(self, name, surname, employee_id, teacher_id):
        super().__init__(name, surname, employee_id)
        self.teacher_id = teacher_id 
    def get_info(self) -> str:
        return f"{super().get_info()}, Teacher ID: {self.teacher_id}"

class Freelance(Employee):
    def __init__(self, name, surname, employee_id, freelance_id):
        super().__init__(name, surname, employee_id)
        self.freelance_id = freelance_id 
    def get_info(self) -> str:
        return f"{super().get_info()}, Freelance ID: {self.freelance_id}"

# test
student = Student("John", "Doe", "12345")
employee = Employee("Jane", "Doe", "67890")
teacher = Teacher("Bob", "Doe", "12345", "98765")
freelance = Freelance("Alice", "Doe", "67890", "54321")

print(student.get_info())
print(employee.get_info())
print(teacher.get_info())
print(freelance.get_info())
