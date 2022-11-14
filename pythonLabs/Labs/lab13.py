
def lab13_task1():
    class Cat:
        def __init__(self, name, color, weight):
            self.name = name
            self.color = color
            self.weight = weight

        def meow(self):
            print(f"Кот по имени {self.name}, весом {self.weight} кг и цветом {self.color}, мяукнул")

    kitten = Cat("Алеша", "белый", 50)
    kitten.meow()

def lab13_task2():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")
    animal = Animal("Данила")
    print(animal.get_name())
    animal.set_name("Максим")
    animal.eat()
    animal.make_noise()


def lab13_task3():
    class StringVar:
        def __init__(self, text):
            self.string = str(text)

        def set(self, text):
            self.string = text

        def get(self):
            return self.string
    string = StringVar("один")
    print(string.get())
    string.set("два")
    print(string.get())


def lab13_task4():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Point(self.x - other.x, self.y - other.y)

        def __mul__(self, other):
            return Point(self.x * other.x, self.y * other.y)

        def __truediv__(self, other):
            return Point(self.x / other.x, self.y / other.y)

        def __floordiv__(self, other):
            return Point(self.x // other.x, self.y // other.y)

        def __mod__(self, other):
            return Point(self.x % other.x, self.y % other.y)

        def __pow__(self, other):
            return Point(self.x ** other.x, self.y ** other.y)

        def __lt__(self, other):
            return self.x < other.x and self.y < other.y

        def __le__(self, other):
            return self.x <= other.x and self.y <= other.y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __ne__(self, other):
            return self.x != other.x and self.y != other.y

        def __gt__(self, other):
            return self.x > other.x and self.y > other.y

        def __ge__(self, other):
            return self.x >= other.x and self.y >= other.y

    point1 = Point(1, 2)
    point2 = Point(3, 4)
    print(point1 + point2)
    print(point1 - point2)
    print(point1 * point2)
    print(point1 / point2)
    print(point1 // point2)
    print(point1 % point2)
    print(point1 ** point2)
    print(point1 < point2)
    print(point1 <= point2)
    print(point1 == point2)
    print(point1 != point2)
    print(point1 > point2)
    print(point1 >= point2)


def lab13_task5():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился кот по имени: {name}, весом {weight} кг, цветом {color}")

        def meow(self):
            print(f"Кот по имени {self.name}, весом {self.weight} кг и цветом {self.color}, мяукнул")

        def make_noise(self):
            print(f"{self.name} говорит: Мяу")
    kitten = Cat("Алеша", "белый", 50)
    kitten.meow()
    kitten.make_noise()


def lab13_task6():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился собака по имени: {name}, весом {weight} кг, цветом {color}")

        def bark(self):
            print(f"Cобака {self.name}, весом {self.weight} кг, цветом {self.color}, гавкнула")

        def make_noise(self):
            print(f"{self.name} говорит: Гав")

    dog = Dog("Алеша", "белый", 50)
    dog.bark()
    dog.make_noise()


def lab13_task7():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился кот по имени: {name}, весом {weight} кг, цветом {color}")

        def meow(self):
            print(f"Кот по имени {self.name}, весом {self.weight} кг и цветом {self.color}, мяукнул")

        def make_noise(self):
            print(f"{self.name} говорит: Мяу")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился собака по имени: {name}, весом {weight} кг, цветом {color}")

        def bark(self):
            print(f"Cобака {self.name}, весом {self.weight} кг, цветом {self.color}, гавкнула")

        def make_noise(self):
            print(f"{self.name} говорит: Гав")

    cat = Cat("жч", "белый", 7)
    cat.set_name("Железный человек")
    cat.meow()
    cat.make_noise()
    dog = Dog("хлк", "черный", 10)
    dog.set_name("Халк")
    dog.bark()
    dog.make_noise()
    dog2 = Dog("анн", "красный", 5)
    dog2.set_name("Анна")
    dog2.bark()
    dog2.make_noise()
    animal = Animal("Александр")
    animal.set_name("Саня")
    animal.make_noise()