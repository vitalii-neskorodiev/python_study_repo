import random

from lesson_22.data_model import Course, session, Student

courses = [
    Course(title='Mathematics'),
    Course(title='Physics'),
    Course(title='Chemistry'),
    Course(title='Biology'),
    Course(title='Computer Science')
]

session.add_all(courses)
session.commit()

for i in range(1, 21):
    student = Student(name=f'Student_{i}')
    student_courses = random.sample(courses, k=random.randint(1, 3))
    student.courses.extend(student_courses)
    session.add(student)

session.commit()


def add_student(name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        print(f"Course '{course_title}' not found.")
        return

    new_student = Student(name=name)
    new_student.courses.append(course)
    session.add(new_student)
    session.commit()
    print(f"Student '{name}' added and enrolled in course '{course_title}'.")


add_student('New Student', 'Mathematics')


def get_students_in_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        print(f"Students enrolled in {course_title}:")
        for student in course.students:
            print(f"- {student.name}")
    else:
        print(f"Course '{course_title}' not found.")


get_students_in_course('Physics')


def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        print(f"Courses for {student_name}:")
        for course in student.courses:
            print(f"- {course.title}")
    else:
        print(f"Student '{student_name}' not found.")


get_courses_for_student('Student_1')


def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"Student name updated from '{old_name}' to '{new_name}'.")
    else:
        print(f"Student '{old_name}' not found.")


update_student_name('New Student', 'Updated Student')


def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student '{name}' has been deleted.")
    else:
        print(f"Student '{name}' not found.")


delete_student('Updated Student')
