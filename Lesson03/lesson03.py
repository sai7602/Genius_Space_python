string = "тестова строка"
if 'тест' in string:
    print(f"Yes {string}")
else:
    print("No{}")

dict = {"name": "John", "age": 23, "city": "New York", "country": "USA", "phone": "123-456-7890"}

for key, value in dict.items():
    print(f"{key}: {value}")


# Парні числа:
number = 50
for i in range(2, number+1, 2):
    print(i)




number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")







#  **Сума чисел:**
list=[]
sum = 0
for num in range(1, 50):
    list.append(num)
    print(list)
    sum = sum+num
    print(sum)
        

#   **Факторіал числа:**
factorial = 1
for num in range(1, 6):
    factorial *= num
    print(factorial)

# **Пошук простих чисел:**
primes = []
for num in range(4, 50):
    if num > 1:  # Перевірка, щоб число було більше 1, бо 1 не є простим числом
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

print(primes) 