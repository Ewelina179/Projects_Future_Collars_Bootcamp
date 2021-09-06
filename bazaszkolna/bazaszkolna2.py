import sys

from baza_classes import Tutor, Teacher, Student, Class_Name

list_of_students = []
list_of_classes = []
list_of_teachers = []
list_of_tutors = []

type_of = sys.argv[1:]

while True:
    types_of_users = ["student <imię nazwisko>", "teacher <imię nazwisko>", "tutor <imię nazwisko>", "end"]
    answer = input(f"Podaj komendę z dostępnych - {types_of_users}: ")
    if answer == "end":
        break
    elif answer.startswith("student"):
        answ = list(answer.split(" "))
        print(answ)
        first_name = answ[1]
        last_name = answ[2]
        class_type = input("Podaj nazwę klasy: ")
        filtered = list(filter(lambda x: x.name == class_type, list_of_classes))
        if filtered:
            x = filtered[0]
            student = Student(first_name, last_name, x)
            x.add_student(student)
        else:
            new_class = Class_Name(class_type)
            student = Student(first_name, last_name, new_class)
            new_class.add_student(student)
            list_of_classes.append(new_class)
        if student not in list_of_students:
            list_of_students.append(student)
    elif answer.startswith("teacher"):
        answ = list(answer.split(" "))
        first_name = answ[1]
        last_name = answ[2]
        subject_name = input("Podaj nazwę przedmiotu: ")
        teacher = Teacher(first_name, last_name, subject_name)
        while True:
            class_type = input("Podaj nazwy klas w kolejnych linijkach: ")
            if class_type == "":
                break
            else:
                filtered = list(filter(lambda x: x.name == class_type, list_of_classes))
                if filtered:
                    x = filtered[0]
                    x.add_teacher(teacher)
                    teacher.add_class_name(x)
                else:
                    new_class = Class_Name(class_type)
                    new_class.add_teacher(teacher)
                    list_of_classes.append(new_class)
                    teacher.add_class_name(new_class)
        if teacher not in list_of_teachers:
            list_of_teachers.append(teacher)
    elif answer.startswith("tutor"):
        answ = list(answer.split(" "))
        first_name = answ[1]
        last_name = answ[2]
        tutor = Tutor(first_name, last_name)
        while True:
            class_type = input("Podaj nazwy klas w kolejnych linijkach: ")
            if class_type == "":
                break
            else:
                filtered = list(filter(lambda x: x.name == class_type, list_of_classes))
                if filtered:
                    x = filtered[0]
                    x.tutor = tutor
                    tutor.add_class_name(x)
                else:
                    new_class = Class_Name(class_type)
                    new_class.tutor = tutor
                    list_of_classes.append(new_class)
                    tutor.add_class_name(new_class)
            if tutor not in list_of_tutors:
                list_of_tutors.append(tutor)

list_of_filtered_objects = [list(filter(lambda x: x.first_name == type_of[0] and x.last_name == type_of[1], list_of_students)), list(filter(lambda x: x.first_name == type_of[0] and x.last_name == type_of[1], list_of_teachers)), list(filter(lambda x: x.first_name == type_of[0] and x.last_name == type_of[1], list_of_tutors)), list(filter(lambda x: x.name == type_of[0], list_of_classes))]

for el in list_of_filtered_objects:
    if el:
        searched_object = el[0]
        if isinstance(searched_object, Student):
            this_student = searched_object
            teachers_of_student = this_student.class_name.teachers
            subjects = this_student.class_name.show_subjects()
            print(f"Nauczyciele to: {teachers_of_student} i prowadzą przedmioty: {subjects}.")
        elif isinstance(searched_object, Teacher):
            this_teacher = searched_object
            x = this_teacher.classes
            tutors_list = []
            for el in x:
                tutors_list.append(el.tutor)
            print(f"Lista wychowawców, z którymi zajęcia prowadzi nauczyciel to: {tutors_list}")
        elif isinstance(searched_object, Tutor):
            tutor = searched_object
            students_list = tutor.show_students()
            print(f"Lista uczniów, których prowadzi wychowawca to: {students_list}")
        elif isinstance(searched_object, Class_Name):
            class_type = searched_object
            tutor_of_class = class_type.tutor
            students = class_type.students
            print(f"Wychowawca to {tutor_of_class}, zaś uczniowie: {students}")
