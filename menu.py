from db import getPassword, savePassword

def menu():
    print("-" * 40)
    print("1. Create / Save new password")
    print("2. Get all passwords")
    print("Q. Exit")
    print("-" * 40)
    return input(": ")

def createPassword():
    url = input("Please enter url or name : ")
    name = input("Please enter username / e-mail : ")
    password = input("Please enter password : ")
    savePassword(url, name, password)

def showPassword():
    data = getPassword()
    for x in data:
        print("-" * 40)
        print("URL / Name : " + x[0])
        print("Username / E-mail : " + x[1])
        print("Password : " + x[2])