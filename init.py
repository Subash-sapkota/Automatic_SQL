import random
import string
from database import do_sql
import time


# Create random nummer of sql table with random table name, random number of columns, random data

# create random name

def random_name(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def random_table_name():
    return random_name(random.randint(5, 10))


def random_columns():
    num_of_columns = random.randrange(2, 6)
    columns = []
    for _ in range(num_of_columns):
        col_name = random_name(random.randint(4, 7))
        col_type = random.choice(["INTEGER", "VARCHAR", "FLOAT"])
        columns.append(f"{col_name} {col_type}")

    return columns


def generate_random_data(columns):
    num_row = random.randint(3, 8)
    data = []

    for _ in range(num_row):
        row = []
        for col in columns:
            if "INTEGER" in col:
                row.append(random.randint(1, 100))
            elif "VARCHAR" in col:
                row.append(random_name(random.randint(1, 7)))
            elif "FLOAT" in col:
                row.append(random.uniform(0, 100))
        data.append(tuple(row))

    return data


def create_table():
    name = random_table_name()
    print(f"Tablename; {name}")
    columns = random_columns()
    print(f"Columns: {columns}")
    sql_create_table = f"CREATE TABLE {name} ({', '.join(columns)});"
    print(f"SQL Create Table: {sql_create_table}")
    do_sql(sql_create_table)

    time.sleep(3)
    insert_data = generate_random_data(columns)
    column_names = [col.split()[0] for col in columns]
    print(f"Columns_Name: {column_names}")
    print(f"data; {insert_data}")
    for data in insert_data:
        placeholders = ', '.join(['%s'] * len(data))
        sql_insert = f"INSERT INTO {name} ({', '.join(column_names)}) VALUES ({placeholders})"
        print(f"SQL Insert: {sql_insert},{data}")
        do_sql(sql_insert,data)


create_table()
