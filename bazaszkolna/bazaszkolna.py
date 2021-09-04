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
        class_name = input("Podaj nazwę klasy: ")
        new_class = Class_Name(class_name)
        student = Student(first_name, last_name, new_class)
        new_class.add_student(student)
        list_of_students.append(student)
        if new_class not in list_of_classes:
            list_of_classes.append(new_class)

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
                for some_class in list_of_classes:
                    if class_type in [x.name for x in list_of_classes]:
                        some_class.add_teacher(teacher)
                        teacher.add_class_name(some_class)
                        teacher.show_classes() # do usunięcia

                    else:
                        new_class = Class_Name(class_type)
                        new_class.add_teacher(teacher)
                        list_of_classes.append(new_class)
                        teacher.add_class_name(new_class)
        if teacher not in list_of_teachers:     
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
                filtered = [filter(lambda x: x.name==class_type, list_of_classes)][0]
                if class_type == filtered:
                    filtered.tutor = tutor
                    tutor.add_class_name(filtered)
                else:
                    new_class = Class_Name(class_type)
                    new_class.tutor = tutor
                    list_of_classes.append(new_class)
                    tutor.add_class_name(new_class)
        if tutor not in list_of_tutors:     
            list_of_tutors.append(tutor)

if type_of == "student":
    first_name = input("Podaj imię: ")
    last_name = input("Podaj nazwisko: ")
    for some_student in list_of_students:
        if some_student.first_name == first_name and some_student.last_name == last_name:
            x = some_student.class_name      
            if isinstance(Class_Name(x), Class_Name):
                print(x)
                teachers = x.show_teachers()
                print(teachers)
                print(x.teachers)
                subjects = []
                for el in teachers:
                    subjects.append(el.subject)
        print(f"Nauczyciele to: {teachers} i prowadzą przedmioty: {subjects}.")
elif type_of == "teacher":
    first_name = input("Podaj imię nauczyciela: ")
    last_name = input("Podaj nazwisko nauczyciela: ")    
    for el in list_of_teachers:
        if el.first_name == first_name and el.last_name == last_name:
            x = el.show_classes()
            print(x)
            tutors_list = []
            for el in x:
                tutors_list.append(el.tutor)
            print(f"Lista wychowawców, z którymi zajęcia prowadzi nauczyciel to: {tutors_list}")
elif type_of == "tutor":
    first_name = input("Podaj imię wychowawcy: ")
    last_name = input("Podaj nazwisko wychowawcy: ")
    filtered = filter(lambda x: x.first_name==first_name and x.last_name==last_name, list_of_tutors)
    if filtered:
        x = list(filtered)[0]
        students_list = []
        for el in x.show_classes():
            print(el.show_students())
            students_list.append(el.show_students())
        print(f"Lista uczniów, których prowadzi wychowawca to: {students_list}")
    else:
        print(f"Nie ma takiego tutora.")
elif type_of == "class_name":
    class_name = input("Podaj nazwę klasy: ")
    for el in list_of_classes:
        if el.name == class_name:
            tutor_of_class = el.tutor
            students = el.show_students()
        print(f"Wychowawca to {tutor_of_class}, zaś uczniowie: {students}") # BRZYDKO ale działa
