from Authorization import *


def main():
    users_list = load_users()       # poziv funkcije za ucitavanje korisnika
    username, password, usertype = login(users_list)        # poziv funkcije za logovanje
    while True:
        if usertype == "m":             # provera da li je korisnik koji se ulogovao menadzer ili prodavac
            if not menu_manager():
                return
            login(users_list)
        else:
            if not menu_salesman():
                return
            login(users_list)


if __name__ == "__main__":
    main()
