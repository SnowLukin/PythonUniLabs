import sqlite3

def get_posts():
    posts = []
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        select_posts = f'select * from Posts'

        cursor.execute(select_posts)

        rows = cursor.fetchall()
        for row in rows:
            posts.append(row)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        temp = []
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            # print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")
        return posts

# MARK: Remove Entity
def remove_article(index):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        remove_article_at_index = f'delete from Article where id = {index}'

        cursor.execute(remove_article_at_index)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        temp = []
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            # print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

def remove_post(index):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        remove_post_at_index = f'delete from Posts where id = {index}'

        cursor.execute(remove_post_at_index)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        temp = []
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            # print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

def remove_user(index):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        remove_user_command = f'delete from Users where id = {index}'

        cursor.execute(remove_user_command)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        temp = []
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            # print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

def remove_recipe(index):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        remove_recipe_at_index = f'delete from Recipes where id = {index}'

        cursor.execute(remove_recipe_at_index)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        temp = []
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            # print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

def remove_ingredient(index):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()
        # print("Подключен к SQLite")

        remove_recipe_at_index = f'delete from Ingredients where id = {index}'

        cursor.execute(remove_recipe_at_index)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        temp = []
        # print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            # print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")

# MARK: Create Entity
def create_post(title, body):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        cursor.execute('select * from Posts')

        row_amount = len(cursor.fetchall()) + 1
        cursor.execute('insert into Posts values(?,?,?);', (row_amount, title, body))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def create_user(name, surname):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        cursor.execute('select * from Users')

        row_amount = len(cursor.fetchall()) + 1
        cursor.execute('insert into Users values(?,?,?);', (row_amount, name, surname))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def create_article(title, body):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        cursor.execute('select * from Articles')

        row_amount = len(cursor.fetchall()) + 1
        cursor.execute('insert into Articles values(?,?,?);', (row_amount, title, body))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def create_ingredient(name: str, price: int):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        cursor.execute('select * from Ingredients')

        row_amount = len(cursor.fetchall()) + 1
        cursor.execute('insert into Ingredients values(?,?,?);', (row_amount, name, price))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def create_recipe(title: str, description: str, cost: int):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        cursor.execute('select * from Recipes')

        row_amount = len(cursor.fetchall()) + 1
        cursor.execute('insert into Recipes values(?,?,?,?);', (row_amount, title, description, cost))
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

# MARK: Edit Entity
def edit_post(index: int, title_: str, body_: str):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        checker = f'select * from Posts where id = {index};'
        cursor.execute(checker)

        change_title = f'update Posts set title = "{title_}" where id = {index};'
        change_body = f'update Posts set body = "{body_}" where id = {index};'
        cursor.execute(change_title)
        cursor.execute(change_body)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def edit_user(index: int, name: str, surname: str):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        checker = f'select * from Users where id = {index};'
        cursor.execute(checker)

        change_title = f'update Users set name = "{name}" where id = {index};'
        change_body = f'update Users set surname = "{surname}" where id = {index};'
        cursor.execute(change_title)
        cursor.execute(change_body)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def edit_article(index: int, title_: str, body_: str):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        checker = f'select * from Articles where id = {index};'
        cursor.execute(checker)

        change_title = f'update Articles set title = "{title_}" where id = {index};'
        change_body = f'update Articles set body = "{body_}" where id = {index};'
        cursor.execute(change_title)
        cursor.execute(change_body)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def edit_ingredient(index: int, name: str, cost: int):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        checker = f'select * from Ingredients where id = {index};'
        cursor.execute(checker)

        change_title = f'update Ingredients set name = "{name}" where id = {index};'
        change_body = f'update Ingredients set price = "{cost}" where id = {index};'
        cursor.execute(change_title)
        cursor.execute(change_body)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def edit_recipe(index: int, title: str, description: str, cost: int):
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        cursor = sqlite_connection.cursor()

        checker = f'select * from Recipes where id = {index};'
        cursor.execute(checker)

        change_title = f'update Recipes set title = "{title}" where id = {index};'
        change_description = f'update Recipes set description = "{description}" where id = {index};'
        change_cost = f'update Recipes set cost = "{cost}" where id = {index};'
        cursor.execute(change_title)
        cursor.execute(change_description)
        cursor.execute(change_cost)

        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        temp = []
    finally:
        if (sqlite_connection):
            sqlite_connection.close()