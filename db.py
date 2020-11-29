import mariadb
import bcrypt

# Connect to database
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="password_manager"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    exit()

# Get Cursor
conn.autocommit = True
cursor = conn.cursor(buffered=True)

def master_password():
    cursor.execute("SELECT password FROM master_password")
    if cursor.rowcount == 0:
        password = input("Please create master password : ")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        cursor.execute("INSERT INTO master_password (password) VALUES (?)", (hashed_password,))
    else:
        password = input("Please enter master password : ")
        if bcrypt.checkpw(password.encode('utf-8'), cursor.fetchone()[0].encode('utf-8')):
            return True
        else:
            return False

def save_password(url, name, password):
    cursor.execute("INSERT INTO password (url, name, password) VALUES (?, ?, ?)", (url, name, password))
    return print("\nPassword has been successfully saved")

def get_password():
    cursor.execute("SELECT url, name, password FROM password")
    return cursor.fetchall()
