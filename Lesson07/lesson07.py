# **Завдання 1: Наслідування**

# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:

# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.") 
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.


# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.
# **Завдання 2: Поліморфізм**

# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").


# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.


# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type  

    def start_engine(self):
        print("Engine started")

    def display_info(self):
        super().display_info()
        print(f"Fuel type: {self.fuel_type}")
    

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size
    def start_engine(self):
        print("Engine started") 
    def display_info(self):
        super().display_info()
        print(f"Engine size: {self.engine_size}")
class Bicycle(Vehicle):
    def __init__(self, make, model, year, wheel_size):
        super().__init__(make, model, year)
        self.wheel_size = wheel_size
    def start_engine(self):
        print("Engine started")
    def display_info(self):
        super().display_info()
        print(f"Wheel size: {self.wheel_size}")
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

car1 = Car("Toyota", "Camry", 2022, "Gasoline")
motorcycle1 = Motorcycle("Honda", "CBR", 2021, "250cc")
bicycle1 = Bicycle("Trek", "Emonda", 2020, "26 inches")

car1.display_info()
motorcycle1.display_info()
bicycle1.display_info()