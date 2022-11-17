# funkcija za prikaz letova koja prima parametar listu letova,
# funkcija prolazi korz listu letova i printa letove u vidu tabele
def load_flights():
    fletovi = open("..\\resources\\flights.txt", "r")
    lista_letova = []
    for let in fletovi.readlines():
        let = let.strip().split("|")
        letovi = {}
        letovi["id"] = let[0]
        letovi["polazak"] = let[1]
        letovi["dolazak"] = let[2]
        letovi["vreme_polaska"] = let[3]
        letovi["vreme_dolaska"] = let[4]
        letovi["aviokompanija"] = let[5]
        letovi["dani"] = let[6]
        letovi["sedista"] = let[7]
        letovi["cena"] = let[8]
        lista_letova.append(letovi)
    return lista_letova


def prikaz_letova(letovi):
    if len(letovi) == 0:
        print("Nema letova")
    else:
        print("{:6} | {} | {} | {} | {:15} | {:15} | {:25} | {} | {}".format("ID", "Polazak", "Dolazak", "Vreme polaska",
                                                                             "Vreme dolaska",
                                                                             "Aviokompanija", "Dani letenja", "Sedista",
                                                                             "Cena"))
        print("=" * 125)
        for x in letovi:
            f = "{id} | {polazak:7} | {dolazak:7} | {vreme_polaska:13} | {vreme_dolaska:15} |" \
                " {aviokompanija:15} | {dani:25} | {sedista:7} | {cena}".format(**x)
            print(f)
            print("-" * 125)


l = load_flights()


def pretraga_letova(letovi):
    print("6 ==> Aviokompanija")
    command = int(input("Unesite broj za pretragu: "))
    try:
        if command == 6:
            aviokomp = input("Unesite ime aviokompanije: ")
            lista = []
            for let in letovi:
                aviokompaija = let["aviokompanija"]
                if aviokomp == aviokompaija:
                    lista.append(let)
            prikaz_letova(lista)
    except:
        print("Pogresan unos")


pretraga_letova(l)
