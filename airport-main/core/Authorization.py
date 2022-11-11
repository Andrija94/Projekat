def menuManager():
    print("Meni za menadzera")
    return

def menuSalesman():
    print("Meni za prodavca")
    return

def login():
    file = open("..\\resources\\users.txt", "r")
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    for lines in file.readlines():
        lines = lines.strip().split("|")
        if username == lines[1] and password == lines[2]:
            print("Prijava je uspesna")
            if lines[0] == "m":
                print("Prijavili ste se kao menadzer")
                menuManager()
            elif lines[0] == "p":
                print("Prijavili ste se kao prodavac")
                menuSalesman()
            return
    print("Prijava nije uspesna")
    return





