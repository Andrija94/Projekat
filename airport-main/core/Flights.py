def load_flights():  # funkcija ucitava letove iz fajla i pretvra ih u listu recnika gde je svaki recnik jedan let
    file_flights = open("..\\resources\\flights.txt", "r")
    list_of_flights = []
    for flight in file_flights.readlines():
        flight = flight.strip().split("|")
        flights = {"id": flight[0], "polazak": flight[1], "dolazak": flight[2], "vreme_polaska": flight[3],
                   "vreme_dolaska": flight[4], "aviokompanija": flight[5], "dani": flight[6], "sedista": flight[7],
                   "cena": flight[8]}
        list_of_flights.append(flights)
    return list_of_flights


flights_call = load_flights()


def flights_output(
        flights):  # funkicja koristi listu letova koja je dobijena iz pretrage i formatira je za ispis korisniku
    if len(flights) == 0:
        print("Nema letova")
    else:
        print(
            "{:6} | {} | {} | {} | {:15} | {:25} | {:25} | {} | {}".format("ID", "Polazak", "Dolazak", "Vreme polaska",
                                                                           "Vreme dolaska",
                                                                           "Aviokompanija", "Dani letenja", "Sedista",
                                                                           "Cena"))
        print("=" * 135)
        for x in flights:
            f = "{id} | {polazak:7} | {dolazak:7} | {vreme_polaska:13} | {vreme_dolaska:15} |" \
                " {aviokompanija:25} | {dani:25} | {sedista:7} | {cena}".format(**x)
            print(f)
            print("-" * 135)


def search(
        flights):  # funkcija koristi listu svih letova i po odredjenom kriterijumu pretrazuje letove i ispisuje rez
    print("1 ==> Mesto polaska \n"
          "2 ==> Odrediste \n"
          "3 ==>  Vreme polaska\n"
          "4 ==> vreme sletanja \n"
          "5 ==> Dani \n"
          "6 ==> Aviokompanija \n"
          "7 ==> Odjava \n")
    command = int(input("Unesite broj za pretragu: "))
    flist = []
    try:
        if command == 1:  # pretraga po mestu polaska
            departure = input("Unesite naziv aerodroma polaska (velikim slovima): ")
            for f in flights:
                if departure == f["polazak"]:
                    flist.append(f)

        elif command == 2:  # pretraga po mestu dolaska
            arrival = input("Unesite naziv aerodroma odredista (velikim slovima): ")
            for f in flights:
                if arrival == f["dolazak"]:
                    flist.append(f)

        elif command == 3:  # pretraga po vremenu polaska, uzletanja
            dep_time = input("Unesite vreme polaska(xx:xx): ")
            for f in flights:
                if dep_time == f["vreme_polaska"]:
                    flist.append(f)

        elif command == 4:  # pretraga po vremenu dolaska, sletanja
            arr_time = input("Unesite vreme sletanja: ")
            for f in flights:
                if arr_time == f["vreme_dolaska"]:
                    flist.append(f)

        elif command == 5:  # pretraga po danima letenja
            days = input("Unesite dan leta (prva tri slova): ")
            for f in flights:
                day = f["dani"].strip().split(",")
                for d in day:
                    if days == d:
                        flist.append(f)

        elif command == 6:  # pretraga po nazivu aviokompanije
            company = input("Unesite ime aviokompanije: ")
            for f in flights:
                if company == f["aviokompanija"]:
                    flist.append(f)

        elif command == 7:  # odjava iz programa
            return 0

        flights_output(flist)  # poziv funkcije koja ispisuje rezultate pretrage
    except:
        print("Pogresan unos")
