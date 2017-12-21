"""sqlite3 built-in module within Python. SQLite allows us to quickly get up and running with databases,
without spinning up larger databases like MySQL or Postgres. """
import sqlite3
from d_b.data_source import Employee

emp1 = Employee('John', 'Travolta', 472346238)
emp2 = Employee('Brad', 'Pit', 800000000)
emp3 = Employee('Angelina', 'Pit', 700000000)

# connection object to represent out lite db
conn = sqlite3.connect(
    ':memory:')  # in momery for testing purposes. creating a new table on each run or save to .db#  file

# cursor which allows us to execute sql queries
cursor = conn.cursor()

# Create Employees table
cursor.execute("""CREATE TABLE Employees (
                  first_name TEXT,
                  last_name TEXT,
                  wage INTEGER

              )""")


def insert_emp(emp):
    with conn:
        cursor.execute('INSERT INTO Employees VALUES (:first, :last, :pay)',
                       {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    cursor.execute("SELECT * FROM Employees WHERE last_name=:last", {'last': lastname})
    return cursor.fetchall()


def update_pay(emp, pay):
    with conn:
        cursor.execute("""UPDATE employees SET wage = :pay
                    WHERE first_name = :first AND last_name = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        cursor.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

insert_emp(emp1)
insert_emp(emp2)
insert_emp(emp3)
update_pay(emp3, 1234)

search = get_emps_by_name('Pit')
print(search)

conn.close()
