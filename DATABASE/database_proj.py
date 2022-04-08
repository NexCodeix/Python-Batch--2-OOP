import sqlite3

conn = sqlite3.connect("db_connection.db")

cursor = conn.cursor()
# CRUD -- > CREATE, RETRIEVE(SELECT), UPDATE, DELETE

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

    def select_data(self, **kwargs):
        if len(kwargs) == 0:
            cursor.execute(f"SELECT * FROM {self.table_name}")

        else:
            query_string = self.query_from_kwargs(kwargs)
            print(query_string)
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE {query_string}")

        data = cursor.fetchall()
        print(data)

    def query_from_kwargs(self, kwargs):
        try:
            q = kwargs.pop("query_condition")
        except KeyError:
            q = "AND"

        vals = list(kwargs.values())
        keys = list(kwargs.keys())

        query_string = ""
        for i in range(len(vals)):
            each_key = keys[i]
            each_val = vals[i]

            if query_string == "":
                query_string += f"{each_key}='{each_val}'"
            else:
                query_string += f" {q} {each_key}='{each_val}'"

        return query_string

    def delete_data(self, **kwargs):
        if len(kwargs) == 0:
            cursor.execute(f"DELETE FROM {self.table_name}")
        else:
            query_string = self.query_from_kwargs(kwargs)
            cursor.execute(f"DELETE FROM {self.table_name} WHERE {query_string}")


db = DbTable("Students", "name:TEXT", "age:INTEGER", "contact:TEXT", "DateOfBirth:TEXT")
db.create_table()
db.add_columns()
db.insert_data("John", 50, 123, "15.09.2000")
db.select_data()
# db.delete_data()

conn.commit()
conn.close()
