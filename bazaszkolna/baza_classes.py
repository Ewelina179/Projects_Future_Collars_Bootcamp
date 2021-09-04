
class Class_Name:
    def __init__(self, name, tutor=None):
        self.name = name
        self.tutor = tutor
        self.teachers = []
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_tutor(self, tutor):
        self.tutors.append(tutor)

    def show_subjects(self):
        subjects = []
        for x in self.teachers:
            subjects.append(x.subject)
        return subjects


class Tutor:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.classes = []

    def add_class_name(self, class_name):
        self.classes.append(class_name)

    def show_students(self):
        students = []
        for x in self.classes:
            students.append(x.students)
        return students

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher:

    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes = []

    def add_class_name(self, class_name):
        self.classes.append(class_name)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Student:

    def __init__(self, firts_name, last_name, class_name):
        self.first_name = firts_name
        self.last_name = last_name
        self.class_name = class_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"