import sqlite3
import bcrypt


conn = sqlite3.connect('password_manager.db')

cursor = conn.cursor()

def create_tables():
    # Izveido master paroles tabulu ja neeksistē
    cursor.execute('''CREATE TABLE IF NOT EXISTS master_password (
                    id integer PRIMARY KEY,
                    password varchar(255) NOT NULL
                );''')
    # Izveido paroļu tabulu ja neeksistē
    cursor.execute('''CREATE TABLE IF NOT EXISTS password (
                    id integer PRIMARY KEY,
                    url varchar(255) NOT NULL,
                    name varchar(255) NOT NULL,
                    password binary NOT NULL
                );''')
    
    
def master_password():
    cursor.execute("SELECT password FROM master_password")
    row = cursor.fetchall()
    if len(row) == 0:
        password = input("Please create master password : ")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        cursor.execute("INSERT INTO master_password (password) VALUES (?)", (hashed_password,))
        conn.commit()
        return True
    else:
        password = input("Please enter master password : ")
        if bcrypt.checkpw(password.encode(), row[0][0]):
            return True
        else:
            return False

def save_password(url, name, password):
    cursor.execute("INSERT INTO password (url, name, password) VALUES (?, ?, ?)", (url, name, password))
    conn.commit()
    return print("\nPassword has been successfully saved")

def get_password():
    cursor.execute("SELECT url, name, password FROM password")
    return cursor.fetchall()