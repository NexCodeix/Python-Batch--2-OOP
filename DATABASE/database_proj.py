import sqlite3

conn = sqlite3.connect("db_connection.db")

cursor = conn.cursor()


class DbTable:
    table_name = None
    columns = []

    def __init__(self, table_name, *args):
        self.table_name = table_name
        self.columns = list(args)
        column_list = []
        for col in args:
            col_name, col_type = col.split(":")
            column_list.append(col_name)

        self.column_list = column_list

    def create_table(self):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
            "Id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
        )""")

    def add_columns(self):
        cols = self.columns
        for col in cols:
            col_name, col_type = col.split(":")
            try:
                cursor.execute(f"""ALTER TABLE {self.table_name} ADD COLUMN {col_name} {col_type}""")
            except sqlite3.OperationalError:
                pass

        return cols           


    def insert_data(self, *args):
        print(tuple(args))
        cols = str(tuple(self.column_list))
        print(cols)
        # a = ", ".join("?" for i in range(vals))

        vals = ""
        for i in range(len(args)):
            vals = vals + "?, "

        vals = vals[:-2]

        cursor.execute(f"""
            INSERT INTO {self.table_name} {cols} VALUES ({vals})
        """, tuple(args))

db = DbTable("Students", "name:TEXT", "age:INTEGER", "contact:TEXT", "DateOfBirth:TEXT")
db.create_table()
db.add_columns()
db.insert_data("John", 50, 123, "15.09.2000")

conn.commit()
conn.close()
