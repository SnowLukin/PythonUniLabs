import sqlite3

def sqlite_sample_table_command(name):
    sqlite_command = f'''CREATE TABLE {name} (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        surname TEXT NOT NULL,
                                        salary REAL NOT NULL);'''
    return sqlite_command

def create_data_base_with_five_tables():
    try:
        sqlite_connection = sqlite3.connect('../sqlite_python.db')
        names = ['first_table', 'second_table', 'third_table', 'fourth_table', 'fifth_table']
        sqlite_create_tables = [sqlite_sample_table_command(name) for name in names]
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        for table in sqlite_create_tables:
            cursor.execute(table)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert_data_to_table(table_name):
    try:
        sqlite_connection = sqlite3.connect('../sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        data = [
            (1, 'One', 'OneOne', 1000),
            (2, 'Two', 'TwoTwo', 2000),
            (3, 'Three', 'ThreeThree', 3000),
            (4, 'Four', 'FourFour', 4000),
            (5, 'Five', 'FiveFive', 5000),
            (6, 'Six', 'SixSix', 6000),
            (7, 'Seven', 'SevenSeven', 7000),
            (8, 'Eight', 'EightEight', 8000),
            (9, 'Nine', 'NineNine', 9000),
            (10, 'Ten', 'TenTen', 10000)
        ]
        cursor.executemany(f'INSERT INTO {table_name} VALUES(?,?,?,?);', data)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def actions_with_data_base(table_name):
    try:
        sqlite_connection = sqlite3.connect('../sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_command_1 = f"""SELECT count(*) from {table_name}"""
        cursor.execute(sqlite_select_command_1)
        total_rows = cursor.fetchone()
        print("Кол-во строк: ", total_rows)

        sql_update_command_1 = f"""Update {table_name} set salary = 999999 where id = 4"""
        sql_update_command_2 = f"""Update {table_name} set name = 'ChangedName' where id = 4"""
        sql_update_command_3 = f"""Update {table_name} set surname = 'ChangedSurname' where id = 4"""
        sql_update_command_4 = f"""Update {table_name} set salary = 10 where salary = 10000"""
        sql_update_command_5 = f"""Update {table_name} set name = 'Changed_Name_Ten' where salary = 10000"""
        sql_update_command_6 = f"""Update {table_name} set surname = 'Changed_Surname_Ten' where salary = 10000"""
        sql_update_command_7 = f"""Update {table_name} set id = 100 where id = 9"""
        cursor.execute(sql_update_command_1)
        cursor.execute(sql_update_command_2)
        cursor.execute(sql_update_command_3)
        cursor.execute(sql_update_command_4)
        cursor.execute(sql_update_command_5)
        cursor.execute(sql_update_command_6)
        cursor.execute(sql_update_command_7)

        sql_delete_command_1 = f"""DELETE from {table_name} where id = 1"""
        sql_delete_command_2 = f"""DELETE from {table_name} where id = 2"""
        sql_delete_command_3 = f"""DELETE from {table_name} where id = 3"""
        sql_delete_command_4 = f"""DELETE from {table_name} where id = 5"""
        cursor.execute(sql_delete_command_1)
        cursor.execute(sql_delete_command_2)
        cursor.execute(sql_delete_command_3)
        cursor.execute(sql_delete_command_4)

        sqlite_select_command_2 = f"""SELECT count(*) from {table_name}"""
        cursor.execute(sqlite_select_command_2)
        total_rows = cursor.fetchone()
        print("Кол-во строк: ", total_rows)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def lab15():
    # create_data_base_with_five_tables()  # Creating 5 tables
    tables = ['first_table', 'second_table', 'third_table', 'fourth_table', 'fifth_table']
    # for table in tables:
    #     insert_data_to_table(table)  # Adding data to existing tables
    actions_with_data_base(tables[4])