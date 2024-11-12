import utilities
# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.

numbers = [1, 2, 3, 4, 5]
average = utilities.calculate_average(numbers)
max_number = utilities.find_max(numbers)
print("Середнє значення:", average)
print("Найбільше число:", max_number)   