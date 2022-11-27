import sqlite3

ingredients = [
    (1, 'Капуста', 50),
    (2, 'Помидор', 500),
    (3, 'Огурец', 10),
    (4, 'Сыр', 290),
    (5, 'Молоко', 20),
    (6, 'Лимон', 30),
    (7, 'Яблоко', 60),
    (8, 'Груша', 80),
    (9, 'Картофель', 40),
    (10, 'Курица', 400),
]
users = [
    (1, 'Snow', 'Lukin'),
    (2, 'Ivan', 'Ivanov'),
    (3, 'Max', 'Max'),
    (4, 'Jessy', 'Jessy'),
    (5, 'Mary', 'Mary'),
    (6, 'Nichol', 'Nichol'),
    (7, 'Ryan', 'Ryan'),
    (8, 'Vlad', 'Vlad'),
    (9, 'Jimmy', 'Jimmy'),
    (10, 'Dave', 'Dave')
]
recipes = [
    (1, 'Chicken soup', 'bla bla bla', 1000),
    (2, 'Salad', 'bla bla bla', 100),
    (3, 'Poison', 'bla bla bla', 600),
    (4, 'Chicken soup', 'bla bla bla', 200),
    (5, 'Chicken soup', 'bla bla bla', 100),
    (6, 'Chicken soup', 'bla bla bla', 300),
    (7, 'Chicken soup', 'bla bla bla', 3000),
    (8, 'Chicken soup', 'bla bla bla', 1000),
    (9, 'Chicken soup', 'bla bla bla', 30),
    (10, 'Chicken soup', 'bla bla bla', 2000)
]
posts = [
    (1, 'Test1', 'Test post 1'),
    (2, 'Test2', 'Test post 2'),
    (3, 'Test3', 'Test post 3'),
    (4, 'Test4', 'Test post 4'),
    (5, 'Test5', 'Test post 5'),
    (6, 'Test6', 'Test post 6'),
    (7, 'Test7', 'Test post 7'),
    (8, 'Test8', 'Test post 8'),
    (9, 'Test9', 'Test post 9'),
    (10, 'Test10', 'Test post 10')
]
articles = [
    (1, 'Article 1', 'body'),
    (2, 'Article 2', 'body'),
    (3, 'Article 3', 'body'),
    (4, 'Article 4', 'body'),
    (5, 'Article 5', 'body'),
    (6, 'Article 6', 'body'),
    (7, 'Article 7', 'body')
]


def fill_sample_tables():
    try:
        sqlite_connection = sqlite3.connect('ProChef_DataBase.db')
        # tables = [users_table, ingredients_table, recipes_table, posts_table, books_table]
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        # for table in tables:
            # cursor.execute(table)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.executemany('insert into Users values(?,?,?);', users)
        cursor.executemany('insert into Ingredients values(?,?,?);', ingredients)
        cursor.executemany('insert into Recipes values(?,?,?,?);', recipes)
        cursor.executemany('insert into Posts values(?,?,?);', posts)
        cursor.executemany('insert into Articles values (?,?,?);', articles)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


# fill_sample_tables()