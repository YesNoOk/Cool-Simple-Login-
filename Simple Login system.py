# start
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from os import system, name
from time import sleep

users = {}
status = ""




def displayMenu():

    print('''================================================================================ 
================================================================================''')

    text = " Simple Login System"  # เขียนข้อความที่เราต้องการเลยนะครับ
    cprint(figlet_format(text, font="small"), "green")  # สามารถเปลียน font ได้นะ กับ สี เปลียนจาก น้ำเงิน เป็น

    print('''================================================================================ 
================================================================================''')

    status = input("                      == LOGIN = l / REGISTER = t ===>  ")
    if status == "l":
        oldUser()
    elif status == "t":
        newUser()
        sleep(5)
    system('cls')



def newUser():
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created\n")


def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        sys.exit(0)
    else:
        print("\nUser doesn't exist or wrong password!\n")


while status != "q":
    displayMenu()

