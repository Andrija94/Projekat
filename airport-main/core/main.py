import Tickets
from Authorization import *


def main():
    users_list = load_users()
    username, password, usertype = login(users_list)
    while True:
        if usertype == "m":
            if not menu_manager():
                return
            login(users_list)
        else:
            if not menu_salesman():
                return
            login(users_list)


if __name__ == "__main__":
    main()
