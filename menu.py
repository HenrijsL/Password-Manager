from random import choice
from crypto import encrypt_message, decrypt_message
from db import get_password, save_password
import random, string, clipboard

def menu():
    print("-" * 40)
    print("1. Create / Save new password")
    print("2. Get all passwords")
    print("Q. Exit")
    print("-" * 40)
    return input(": ")

def create_password_menu():
    print("1. Enter your own password")
    print("2. Generate random password")
    return input(": ")

def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for i in range(length)))

def create_password():
    url = input("Please enter url or name : ")
    name = input("Please enter username / e-mail : ")
    choice = create_password_menu()
    while True:
        if choice == "1":
            password = input("Please enter password : ")
            break
        if choice == "2":
            length = input("Please enter password lenght : ")
            password = generate_password(int(length))
            print("Your password is : " + password)
            clipboard.copy(password)
            print("Password has been successfully saved to clipboard")
            break
        choice = create_password_menu()
    token = encrypt_message(password)
    save_password(url, name, token)

def show_password():
    data = get_password()
    for x in data:
        print("-" * 40)
        print("URL / Name : " + x[0])
        print("Username / E-mail : " + x[1])
        print("Password : " + decrypt_message(x[2]))
