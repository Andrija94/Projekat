# funkcija za prikaz letova koja prima parametar listu letova,
# funkcija prolazi korz listu letova i printa letove u vidu tabele
letovi = open("..\\resources\\flights.txt", "r")
lista_letova = []
for let in letovi.readlines():
    lista_letova.append(let)
    print(let)

