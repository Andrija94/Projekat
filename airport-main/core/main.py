import Tickets
from Authorization import *


def main():
    users = open("..\\resources\\users.txt", "r")
    usersList = []
    for user in users:
        usersList.append(user.strip().split("|"))
    username, password, usertype = login(usersList)
    while True:
        if usertype == "m":
            if not menuManager():
                return
            login(usersList)
        else:
            if not menuSalesman():
                return
            login(usersList)


if __name__ == "__main__":
    main()
