import sqlite3

conn = sqlite3.connect("connection_test.db")

cursor = conn.cursor()

def create_table(table_name):
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
        "Id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name TEXT NOT NULL,
        Age INTEGER NOT NULL,
        Height REAL NOT NULL
    )""")


def insert_data(name, age, height):
    cursor.execute(f"""
        INSERT INTO Students (Name, Age, Height) VALUES (:n, :a, :h)
    """, {
        "n": name,
        "a": age,
        "h": height
    })
    conn.commit()


def select_data():
    cursor.execute(f"""
        SELECT * FROM Students
    """)
    data = cursor.fetchall()
    for d in data:
        print(d)


def enter_data():
    name_inp = input("Emter your name: ")
    age_inp = input("Emter your age: ")
    height_inp = input("Emter your height: ")
    return insert_data(name_inp, age_inp, height_inp)

def enter_table_name():
    table_name = input("Enter Your Table Name: ")
    create_table(table_name)


while True:
    command = input("Enter your command: ")
    if command == "q":
        break

    command_dict = {
        "insert": enter_data,
        "fetch": select_data,
        "create": enter_table_name
    }

    command_dict[command]()  # insert_data()


conn.commit()
cursor.close()
conn.close()
