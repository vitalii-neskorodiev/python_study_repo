# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:

    def __init__(self, name: str, surname: str, age: int, average_grade: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def average_grade_changed(self, new_average_grade: float):
        self.average_grade = new_average_grade


student_1 = Student("Tommy", "Vercetti", 21, 10.35)
print(student_1.name, student_1.surname, student_1.age, student_1.average_grade)

student_1.average_grade_changed(10.5)

print(student_1.name, student_1.surname, student_1.age, student_1.average_grade)
