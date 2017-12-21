import sqlite3

# connect to local db
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# make table
cursor.execute("""CREATE TABLE Donors (
                  first_name TEXT,
                  last_name TEXT,
                  email TEXT

              )""")


def insert(first_name, last_name, email):
    with conn:
        cursor.execute('INSERT INTO Donors VALUES (:first_name, :last_name, :email)',
                       {'first_name': first_name, 'last_name': last_name, 'email': email})


def get_by_lastname(lastname):
    cursor.execute("SELECT * FROM Donors WHERE last_name=:lastname", {'lastname': lastname})
    return cursor.fetchall()


def get_by_email(email):
    cursor.execute("SELECT * FROM Donors WHERE email=:email", {'email': email})
    return cursor.fetchall()


def get_all():
    cursor.execute('SELECT * FROM Donors')
    return cursor.fetchall()


def update_email(firstname, lastname, email):
    with conn:
        cursor.execute("""UPDATE Donors SET email = :email
                    WHERE first_name = :first AND last_name = :last""",
                       {'first': firstname, 'last': lastname, 'email': email})


def remove_donor(email):
    with conn:
        cursor.execute("DELETE FROM Donors WHERE email = :email",
                       {'email': email})
