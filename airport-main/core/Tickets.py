def load_tickets():  # funkcija koja ce ucitati sve karte iz fajla tickets.txt
    file_tickets = open("..\\resources\\tickets.txt", "r")
    list_of_tickets = []
    for ticket in file_tickets.readlines():
        ticket = ticket.strip().split("|")
        tickets = {"id": ticket[0], "polazak": ticket[1], "dolazak": ticket[2],
                   "vreme_polaska": ticket[3],
                   "vreme_dolaska": ticket[4], "aviokompanija": ticket[5], "dan": ticket[6], "red": ticket[7],
                   "sediste": ticket[8], "cena": ticket[9], "broj_karte": ticket[10]}
        list_of_tickets.append(tickets)
    return list_of_tickets


def ticket_save(ticket):  # funkcija prikazuje izabranu kartu i cuva je u fajl tickets.txt
    print('Rezervisana je karta:')
    print("{:6}|{}|{}|{}|{:15}|{:25}|{:5}|{:5}|{:10}|{}|{}".format('ID', 'Polazak', 'Dolazak', 'Vreme polaska',
                                                                   'Vreme dolaska',
                                                                   'Aviokompanija', 'Dan', 'Red', 'Sediste',
                                                                   'Cena', 'Broj karte'))
    print("=" * 115)
    format_ticket = "{}|{:7}|{:7}|{:13}|{:15}|{:25}|{:5}|{:5}|{:10}|{}|{}".format(ticket[0], ticket[1], ticket[2],
                                                                                  ticket[3], ticket[4],
                                                                                  ticket[5], ticket[6], ticket[7],

                                                                                  ticket[8], ticket[9], ticket[10])
    print(format_ticket)

    ticket_to_save = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4],
                                                               ticket[5], ticket[6], ticket[7],
                                                               ticket[8], ticket[9], ticket[10])
    file_tickets = open("..\\resources\\tickets.txt", 'a')
    file_tickets.write(ticket_to_save + '\n')


def ticket_remove(tickets):
    file_tickets = open("..\\resources\\tickets.txt", "r+")
    file_tickets.truncate(0)
    for ticket in tickets:
        t = "{id}|{polazak}|{dolazak}|{vreme_polaska}|{vreme_dolaska}|{aviokompanija}|" \
            "{dan}|{red}|{sediste}|{cena}|{broj_karte}".format(**ticket)
        file_tickets.write(t + "\n")
    print("Karta je uspesno izbrisana!")


def ticket_input(flight_list):  # funkcija za unos karte, radi proveru da li karta postoji ili ne
    ticket_list = load_tickets()
    ticket_id = input("Unesite ID leta u formatu XX1234: ")
    day = input("Unesite dan leta(prva tri slova): ")
    row = int(input("Unesite broj reda: "))
    seat = int(input("Unesite broj sedista: "))
    for ticket in ticket_list:
        if ticket_id == ticket['id'] and day == ticket['dan'] and row == int(ticket['red']) and \
                seat == int(ticket['sediste']):
            print('Karta je vec rezervisana!')
            return

    if not ticket_list:
        ticket_number = len(ticket_list) + 1
    else:
        ticket_number = int(ticket_list[len(ticket_list) - 1]["broj_karte"]) + 1

    for flight in flight_list:  # ukoliko karta ne postoji u fajlu onda izvlaci podatke za taj let
        days = flight['dani'].strip().split(',')
        seats = flight['sedista'].strip().split('/')
        if ticket_id == flight['id'] and day in days and 0 < row <= int(seats[0]) and 0 < seat <= int(seats[1]):
            result = [flight['id'], flight['polazak'], flight['dolazak'],
                      flight['vreme_polaska'], flight['vreme_dolaska'], flight['aviokompanija'],
                      day, str(row), str(seat), flight['cena'], str(ticket_number)]
            ticket_save(result)
            return
    print("Nepostojeci let, pokusajte ponovo!")


def ticket_delete():
    ticket_list = load_tickets()
    ticket_number = int(input("Unesite broj karte: "))
    for ticket in ticket_list:
        if ticket_number == int(ticket["broj_karte"]):
            ticket_list.remove(ticket)
            ticket_remove(ticket_list)
            return
    print("Karta ne postoji u bazi!")
    return
