# Створення моделі даних: Створіть просту модель даних для системи управління студентами.
# Модель може містити таблиці для студентів, курсів та їх відношень. Кожен студент може бути зареєстрований на декілька курсів. Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
# Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до певного курсу.
# Переконайтеся, що ці зміни коректно відображаються у базі даних.
# Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих на певний курс, або курси, на які зареєстрований певний студент.
# Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також видалення студентів з бази даних.from pip._internal.commands import install

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

enrollment_table = Table(
    'enrollment',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=enrollment_table, back_populates='students')


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=enrollment_table, back_populates='courses')


engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
