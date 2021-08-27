import sys
#lista wstępna - stan magazynu słownik. chyba, że czyta z pliku i tam trzymam i na starcie context managera odpalam, żeby wzięło (jak starczy czasu to i dodało do stanu początkowego)
saldo = 1500
magazyn = {"produkt1": 2, "produkt2": 5, "produkt3": 1, "produkt4": 9}
stan_magazynowy_produktu_1 = 0

list_of_logs = []

commands = "saldo", "sprzedaż", "zakup", "konto", "magazyn"

pierwszy_argument = sys.argv[1]

while pierwszy_argument in commands:

    commands2 = "saldo", "zakup", "sprzedaz", "stop"

    answer = input("Podaj komendę z dostepnych: ") #lista dostępnych

    if answer == "saldo": # sprawdzam, czy wykonalne. jeśli takm działam
        pierwsza = int(input("zmiana na koncie wyrażona w groszach"))
        druga = input("komentarz do zmiany")
        
    elif answer == "zakup": # logi do tych akcji - string, zdanie, niecha zapisuje w liście. pickle lub nie.
        product_id = input("Podaj identyfikator produktu: ")
        price = int(input("Podaj cenę jednostkową: "))
        amount = int(input("Podaj liczbę sztuk: "))
        zakup = saldo - price * number

        if saldo < 0:
            print("Saldo nie może być ujemne.")
            break
        elif price < 0:
            print("Cena nie może być ujemna.")
            break
        elif amount < 0:
            print("Liczba sztuk nie może być mniejsza od 0.")
            break
        """
        Jeśli saldo po zmianie jest ujemne, cena jest ujemna bądź liczba sztuk jest mniejsza od zero program zwraca błąd. Program podnosi stan magazynowy zakupionego towaru
        """

        # podnieś stan magazynowy tego towaru!!!

    elif answer == "sprzedaz":
        product_id = input("Podaj identyfikator produktu: ")
        price = int(input("Podaj cenę jednostkową: "))
        number = int(input("Podaj liczbę sztuk: "))
        pass
        """
        Program dodaje do salda cenę jednostkową pomnożoną razy liczbę sztuk. 
         Jeśli na magazynie nie ma wystarczającej liczby sztuk, cena jest ujemna bądź liczba sztuk sprzedanych jest mniejsza od zero program zwraca błąd. Program obniża stan magazynowy zakupionego towaru.
         """
    elif answer == "stop": # od razu robi te z sys.argv
        continue

    else:

        break

# robi co z sys argv
    if sys.argv[1] == "saldo":
        wartosc = int(sys.argv[2])
        komentarz = int(sys.argv[3])
        pass
    elif sys.argv[1] == "sprzedaż": # uwględnić obsługę wyjątków i walidację???
        identyfikator_produktu = sys.argv[2] # str ma być
        cena = int(sys.argv[3])
        liczba_sprzedanych = int(sys.argv[4])
    elif sys.argv[1] == "zakup":
        identyfikator_produktu = sys.argv[2]
        cena = int(sys.argv[3])
        liczba_zakupionych = int(sys.argv[4])
    elif sys.argv[1] == "konto":
        pass
    elif sys.argv[1] == "magazyn":
        identyfikator_produktu = sys.argv[2]
        identyfikator_produktu = sys.argv[3] # tu pętla czy co? można by funkcje i args
        pass
    elif sys.argv[1] == "przegląd":
        pass
    else:
        break

else:
    print("Niedozwolona komenda.")

