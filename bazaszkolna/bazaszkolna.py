import sys

from baza_classes import Tutor, Teacher, Student, Class_Name

list_of_students = []
list_of_classes = []
list_of_teachers = []
list_of_tutors = []

TYPE = ("student", "teacher", "tutor", "class_name")

type_of = sys.argv[1]

while type_of in TYPE:

    types_of_users = ("student", "teacher", "tutor", "end")

    answer = input("Podaj komendę z dostepnych: ") 

    if answer not in types_of_users:
        print("Niewłaściwa komenda.")
        continue

    if answer not in types_of_users:
        print("Niewłaściwy typ uzytkownika.")
        continue
    elif answer == "end":
        break

    elif answer == "student":
        first_name = input("Podaj imię: ")
        last_name = input("Podaj nazwisko: ")
        class_type = input("Podaj nazwę klasy: ")
        filtered = list(filter(lambda x: x.name==class_type, list_of_classes))
        if filtered:
            x = list(filtered)[0]
            student = Student(first_name, last_name, filtered)
            x.add_student(student)
            
        else:
            new_class = Class_Name(class_type)
            student = Student(first_name, last_name, new_class)
            new_class.add_student(student)
            list_of_classes.append(new_class)
            
        if student not in list_of_students:
            list_of_students.append(student) # chyba do poprawki!!! 

    elif answer == "teacher":
        first_name = input("Podaj imię: ")
        last_name = input("Podaj nazwisko: ")
        subject_name = input("Podaj nazwę przedmiotu: ")
        teacher = Teacher(first_name, last_name, subject_name)
        while True:
            class_type = input("Podaj nazwy klas w kolejnych linijkach: ")
            if class_type == "":
                break
            else:
                filtered = list(filter(lambda x: x.name==class_type, list_of_classes))
                if filtered:
                    x = filtered[0]
                    x.add_teacher(teacher)
                    teacher.add_class_name(x)
                else:
                    new_class = Class_Name(class_type)
                    new_class.add_teacher(teacher)
                    list_of_classes.append(new_class)
                    teacher.add_class_name(new_class)
        if teacher not in list_of_teachers:     # to źle
            list_of_teachers.append(teacher)

    elif answer == "tutor":
        first_name = input("Podaj imię: ")
        last_name = input("Podaj nazwisko: ")
        tutor = Tutor(first_name, last_name)
        while True:
            class_type = input("Podaj nazwy klas w kolejnych linijkach: ")
            if class_type == "":
                break
            else:
                filtered = list(filter(lambda x: x.name==class_type, list_of_classes))
                if filtered:
                    x = filtered[0]
                    x.tutor = tutor
                    tutor.add_class_name(filtered)
                else:
                    new_class = Class_Name(class_type)
                    new_class.tutor = tutor
                    list_of_classes.append(new_class)
                    tutor.add_class_name(new_class)
        if tutor not in list_of_tutors:     # chyba poprawka
            list_of_tutors.append(tutor)

if type_of == "student":
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    filtered = list(filter(lambda x: x.first_name==first_name and x.last_name==last_name, list_of_students))
    if filtered:
        this_student = filtered[0]
        teachers_of_student=this_student.class_name.teachers
        subjects=this_student.class_name.show_subjects()
    else:
        print("Nie ma takiego ucznia.")
    print(f"Nauczyciele to: {teachers_of_student} i prowadzą przedmioty: {subjects}.")
    

elif type_of == "teacher":
    first_name = input("Podaj imię nauczyciela: ")
    last_name = input("Podaj nazwisko nauczyciela: ")    
    filtered = list(filter(lambda x: x.first_name==first_name and x.last_name==last_name, list_of_teachers))
    if filtered:
        this_teacher = filtered[0]
        x = this_teacher.classes
        tutors_list = []
        for el in x:
            tutors_list.append(el.tutor)
        print(f"Lista wychowawców, z którymi zajęcia prowadzi nauczyciel to: {tutors_list}")

elif type_of == "tutor":
    first_name = input("Podaj imię wychowawcy: ")
    last_name = input("Podaj nazwisko wychowawcy: ")
    filtered = list(filter(lambda x: x.first_name==first_name and x.last_name==last_name, list_of_tutors))
    if filtered:
        tutor = filtered[0]
        print(tutor.show_students()) # wyprintowało reprezentację tutora #  po tej stronie jakiś błąd. bo w klasie dobrze AttributeError: 'list' object has no attribute 'students' - a przecież dodaję obiekty całe (klasy)
        students_list = tutor.show_students()
        print(f"Lista uczniów, których prowadzi wychowawca to: {students_list}")
    else:
        print(f"Nie ma takiego tutora.")

elif type_of == "class_name":
    class_name = input("Podaj nazwę klasy: ")
    filtered = list(filter(lambda x: x.name==class_name, list_of_classes))
    if filtered:
        class_type = filtered[0]
        tutor_of_class = class_type.tutor
        students = class_type.students
    print(f"Wychowawca to {tutor_of_class}, zaś uczniowie: {students}")
