how_much_packages=int(input("Podaj liczbę paczek do wysłania: "))
number_of_packages=0 # całkowita liczba wysłanych paczek
whole_weight=0 # liczba wysłanych kilogramów
current_package=0 # bieżąca paczka - licznik wagi
lightest_packages = 20

while number_of_packages < how_much_packages:
    
    how_is_weight=int(input("Podaj masę towaru: "))
    if how_is_weight==0:
        number_of_packages += 1
        whole_weight += current_package
        if lightest_packages > current_package:
                lightest_packages = current_package
        print("Zadanie zakończono. ")
        break
    if 1<how_is_weight>10:
        print("Operacja niedozwolona.")
        continue
    else:
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
            current_package=0
        elif current_package < 20:
            current_package += how_is_weight

empty = number_of_packages * 20 - whole_weight # liczba "pustych" kilogramów
print(f"Liczba paczek wysłanych {number_of_packages}, liczba wysłanych kg {whole_weight}, najlżejsza paczka wazyła {lightest_packages} kg. Brak optymalnego pakowania spowodował niezapełnienie przestrzeni, która mogłaby ważyć po wykorzystaniu {empty} kg.")


