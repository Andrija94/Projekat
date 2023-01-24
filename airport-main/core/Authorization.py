from Tickets import *


def load_users():  # funkcija ucitava sve korisnike iz fajla i pravi listu sa njihovim kredencijalima i tipom korisnika
    file_users = open("..\\resources\\users.txt", "r")
    users_list = []
    for user in file_users:
        users_list.append(user.strip().split("|"))
    return users_list  # funkcija vraca listu korisnika


def menu_manager():  # funkcija koja sadrzi opcije kojima moze da pristupi menadzer
    while True:
        print("0 ==> Izlaz iz programa\n"
              "1 ==> Pretraga letova\n"
              "2 ==> Istorija\n"
              "9 ==> Odjava")
        try:
            command = int(input("Unesite opciju: "))
            if command == 0:
                return False
            elif command == 1:
                x = search(flights_call)
                if x == 0:
                    return True
            elif command == 9:
                return True
            else:
                print("Pokusajte ponovo")
        except:
            print("Pogresan unos")


def menu_salesman():  # funkcija koja sadrzi opcije kojima moze da pristupi prodavac
    while True:
        print("0 ==> Izlaz iz programa\n"
              "1 ==> Pretraga\n"
              "2 ==> Unos karte\n"
              "3 ==> Izmena karte\n"
              "4 ==> Brisanje karte\n"
              "9 ==> Odjava\n")
        try:
            command = int(input("Unesite opciju: "))
            if command == 0:
                return False
            elif command == 1:
                x = search(flights_call)
                if x == 0:
                    return True
            # elif command == 2:
            #     # ticket_input(flights_call, tickets_call)
            elif command == 9:
                return True
            else:
                print("Pokusajte ponovo")
        except:
            print("Pogresan unos")


def login(ulist):  # funkcija koristi listu svih korisnika i omogucava pristup programu unosom odgovarajucih kredencijala
    while True:
        username = input("Unesite korisnicko ime: ")
        password = input("Unesite lozinku: ")
        for user in ulist:
            if username == user[1] and password == user[2]:
                print("Prijava je uspesna")
                if user[0] == "m":
                    print("Prijavili ste se kao menadzer")
                elif user[0] == "p":
                    print("Prijavili ste se kao prodavac")
                return username, password, user[0]  # funkcija vraca tri vrednosti: korisnicko ime, sifru i tip korisnika
        print("Prijava nije uspesna")
