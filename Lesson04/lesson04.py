# **Робота із списками:** 
#Завдання: Створіть список чисел. Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.


numbers = [1, 2, 3, 4, 5, 6]
numbers.append(10)
numbers.append(20)
numbers.remove(10)
print(numbers)
# **Знаходження суми:**
#   Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.

numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)
#  **Подвійні значення:**
#   Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.

numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)  
#**Робота із кортежами:**
#   Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин"). Виведіть кожен елемент кортежу окремо.

fruits = ("яблуко", "банан", "апельсин")
for fruit in fruits:
    print(fruit)
#   **Об'єднання кортежів:**
#  Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.

numbers = (1, 2, 3)
numbers2 = (4, 5, 6)
combined_numbers = numbers + numbers2
print(combined_numbers)

#**Робота із словниками:**
#  Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена (ім'я, вік, спорт, команда тощо). Виведіть цю інформацію на екран.

sportsman = {
    "name": "John",
    "age": 30,
    "sport": "Football",
    "team": "Manchester United"
}
print(sportsman)

#**Оновлення словника:**
#   Завдання: Створіть словник, що містить ваші улюблені книги (назва книги та рік видання). Додайте до словника нову улюблену книгу та виведіть оновлений словник.

books = {
    "The Great Gatsby": 1925,
    "To Kill a Mockingbird": 1960,
    "1984": 1949
}
books["The Catcher in the Rye"] = 1951
print(books)

#**Пошук значення:**
#    Завдання: Створіть словник, що містить інформацію про країни та їх столиці. Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).

countries = {
    "Ukraine": "Kyiv",
    "Germany": "Berlin",
    "France": "Paris"
}
country = input("Enter a country: ")
if country in countries:
    capital = countries[country]
    print(f"The capital of {country} is {capital}.")
else:
    print("Country not found.") 