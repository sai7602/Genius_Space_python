# Завдання 1: Інкапсуляція

# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)
# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.

from abc import ABC, abstractmethod


class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

# Завдання 2: Абстракція

# Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.

class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius   

class Rectangle(Shape):
    def calculate_area(self, width, height):
        return width * height

class Triangle(Shape):
    def calculate_area(self, base, height):
        return 0.5 * base * height        
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

print(circle.calculate_area(20))
print(rectangle.calculate_area(25, 15))
print(triangle.calculate_area(12, 8))
# Завдання 3: Користування інкапсуляцією та абстракцією у реальному коді


# Розгляньте фрагмент коду з існуючого проекту або бібліотеки та ідентифікуйте в ньому використання інкапсуляції та абстракції. Поясніть, як вони застосовуються і як це допомагає поліпшити читабельність та підтримку коду.