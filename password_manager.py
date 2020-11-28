import db
from db import masterPassword
from menu import createPassword, menu, showPassword

if not masterPassword():
    exit()

choice = menu()

while choice.lower() != "q":
    if choice == "1":
        createPassword()
    if choice == "2":
        showPassword()
    choice = menu()

exit()




