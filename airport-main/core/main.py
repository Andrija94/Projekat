import Tickets
from Authorization import *


def main():
    users = open("..\\resources\\users.txt", "r")
    usersList = []
    for user in users:
        usersList.append(user.strip().split("|"))
    while True:
        username, password, usertype = login(usersList)
        if usertype == "m":
            return menuManager(usersList)
        else:
            menuSalesman()
        break


if __name__ == "__main__":
    main()
