how_much_elements = int(input("Podaj liczbę elementów do wysłania: "))
number_of_packages = 0 # całkowita liczba wysłanych paczek
whole_weight = 0 # liczba wysłanych kilogramów
current_package = 0 # bieżąca paczka - licznik wagi
lightest_packages = 20
empty = number_of_packages * 20 - whole_weight # liczba "pustych" kilogramów
current_number_of_element = 0

while current_number_of_element <= how_much_elements:
    
    how_is_weight=int(input("Podaj masę towaru: "))
    if how_is_weight==0:
        number_of_packages += 1
        whole_weight += current_package
        if lightest_packages > current_package:
                lightest_packages = current_package
        print("Zadanie zakończono. ")
        break
    elif 1<how_is_weight>10:
        number_of_packages = 0
        whole_weight = 0
        empty = 0
        lightest_packages = 0
        print("Operacja niedozwolona.")
        break
    else: #tu zgrzyta. może lecieć pętla o ile bieżąca paczka gdy dodajemy elementy nie przekroczła ilości max elementów do dodania.
        if current_package + how_is_weight > 20:
            number_of_packages += 1
            whole_weight += current_package
            if lightest_packages > current_package:
                lightest_packages = current_package
            current_package = how_is_weight
        elif current_package + how_is_weight == 20:
            number_of_packages += 1
            current_package += how_is_weight
            whole_weight += current_package
            current_number_of_element += 1
            print(current_number_of_element)
            current_package=0
            if current_number_of_element == how_much_elements:
                break
        elif current_package < 20: 
            current_package += how_is_weight
            current_number_of_element += 1
            print(current_number_of_element)
            if current_number_of_element == how_much_elements:
                whole_weight += current_package
                number_of_packages += 1
                break

print(f"Liczba paczek wysłanych {number_of_packages}, liczba wysłanych kg {whole_weight}, najlżejsza paczka wazyła {lightest_packages} kg. Brak optymalnego pakowania spowodował niezapełnienie przestrzeni, która mogłaby ważyć po wykorzystaniu {empty} kg.")

