def load_users():
    file_users = open("..\\resources\\users.txt", "r")
    users_list = []
    for user in file_users:
        users_list.append(user.strip().split("|"))
    return users_list

def menu_manager():
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
                pretraga_letova()
            elif command == 9:
                return True
        except:
            print("Pogresan unos")



def menu_salesman():
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
            elif command == 9:
                return True
        except:
            print("Pogresan unos")


def login(list):
    while True:
        username = input("Unesite korisnicko ime: ")
        password = input("Unesite lozinku: ")
        for user in list:
            if username == user[1] and password == user[2]:
                print("Prijava je uspesna")
                if user[0] == "m":
                    print("Prijavili ste se kao menadzer")
                elif user[0] == "p":
                    print("Prijavili ste se kao prodavac")
                return username, password, user[0]
        print("Prijava nije uspesna")
