

class Tutor:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.classes = []

    def add_class_name(self, class_name):
        self.classes.append(class_name)

    def show_classes(self):
        classes = [x for x in self.classes]
        return classes

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

    def show_classes(self):
        classes = [x for x in self.classes]
        return classes

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student:

    def __init__(self, firts_name, last_name, class_name):
        self.first_name = firts_name
        self.last_name = last_name
        self.class_name = class_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}" #  ma nauczycieli: {self.class_name.tutors}


class Class_Name:
    def __init__(self, name):
        self.name = name
        self.tutors = None
        self.teachers = []
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_tutor(self, tutor):
        self.tutors.append(tutor)

    def show_teachers(self):
        return [x for x in self.teachers]
    
    ### def show_tutors(self):
    ###    tutors = [x for x in self.tutors] # niby powinien być jeden. ale z implementacji nie wynika ograniczenie
    #    return tutors

    def show_students(self):
        students = [x for x in self.students]
        return students