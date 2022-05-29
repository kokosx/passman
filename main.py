from passm import PasswordManager
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

pm=PasswordManager()

#pm.write("gramfgds","mytr","grtsgrse","1htrhr")

def showOptions():
    inp = input("""[q] to go back : """)
    if inp == 'q':
        cls()
        showMenu()

def listMenu():
    res = pm.printAll()
    if res == 1:
        print("")
        showOptions()
    if res == 0:
        cls()
        print('No socials added!')
        showMenu()

def listDelete():
    res = pm.printAll()
    if res == 0:
        cls()
        print('No socials added!')
        showMenu()

def showMenu():
    inp = input("""This is password manager!
Options:
[0]: List all socials
[1]: Add new social
[2]: Delete social
[q]: Quit\n>> """)
    match inp:
        case '0':
            listMenu()
        case '1':
            social = input("Social name: ")
            mail = input("Email: ")
            login = input("Login: ")
            password = input("Password: ")
            pm.write(social,mail,login,password)
            cls()
            print(f"{social} has been added")
            showMenu()
        case '2':
            listDelete()
            social = input("Social to delete: ")
            pm.delete(social)
            cls()
            print(f"{social} has been deleted")
            showMenu()
        case 'q':
            cls()
        case default:
            cls()
            print("Wrong argument")
            showMenu()




cls()
showMenu()