def menuManager():
    print("Meni za menadzera")
    return


def menuSalesman():
    print("Meni za prodavca")
    return


def login(usersList):
    while True:
        username = input("Unesite korisnicko ime: ")
        password = input("Unesite lozinku: ")
        for user in usersList:
            if username == user[1] and password == user[2]:
                print("Prijava je uspesna")
                if user[0] == "m":
                    print("Prijavili ste se kao menadzer")
                elif user[0] == "p":
                    print("Prijavili ste se kao prodavac")
                return username, password, user[0]
        print("Prijava nije uspesna")

