from db import create_tables, master_password
from menu import create_password, menu, show_password

create_tables()

if not master_password():
    exit()

choice = menu()

while choice.lower() != "q":
    if choice == "1":
        create_password()
    if choice == "2":
        show_password()
    choice = menu()

exit()




