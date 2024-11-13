# Завдання 1: Створення класу і об'єктів**

# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:

# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

    def make_sound(self):
        print(f"{self.name} makes a sound!")
# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

animal1 = Animal("Tom", "cat", 3)
animal2 = Animal("Bob", "dog", 5)

animal1.make_sound()
animal2.make_sound()

# **Завдання 2: Робота з об'єктами**

# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height    
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)

# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
    def calculate_area(self):
        return self.width * self.height 
# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, виведіть площу прямокутників на екран.

rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4, 6)    

print(rectangle1.calculate_area())
print(rectangle2.calculate_area())