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


def ticket_save(ticket):
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


def ticket_input(flight_list):
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
    ticket_number = len(ticket_list) + 1
    for flight in flight_list:
        days = flight['dani'].strip().split(',')
        seats = flight['sedista'].strip().split('/')
        if ticket_id == flight['id'] and day in days and 0 < row <= int(seats[0]) and 0 < seat <= int(seats[1]):
            result = [flight['id'], flight['polazak'], flight['dolazak'],
                      flight['vreme_polaska'], flight['vreme_dolaska'], flight['aviokompanija'],
                      day, str(row), str(seat), flight['cena'], str(ticket_number)]
            ticket_save(result)
            return
    print("Nepostojeci let, pokusajte ponovo!")
