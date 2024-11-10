# Funcs for int
num_1 = "1"
print(type(num_1))

num_1 = int(num_1)
print(type(num_1))

num_1 = float(num_1)
print(type(num_1))

# Funcs for string
string = "hello world!"
print(len(string))

string = string.upper()
print(string)

string = string.lower()
print(string)

string = string.capitalize()
print(string)

string = string.replace("!", ".")
print(string)

string = string.split()
print(string)

string = " ".join(string)
print(string)

string = string.count("o")
print(string)

string = 1
string = str(string)
print(type(string))

# Funcs for list
base_list = [1, 2, 3]
print(len(base_list))

base_list.append(4)
print(base_list)

base_list.extend([5, 6, 7])
print(base_list)

print(base_list.index(4))

# Funcs for dict
base_dict = {"name": "Tom", "age": 40, "high": 180}
print(base_dict.keys())
print(base_dict.values())
print(base_dict.items())

print(base_dict["name"], base_dict.get("name"), base_dict.get("is_animal", "No"))
print(base_dict["is_animal"])

lst = [1, 2, 3, 4, 5]
dct = {"name": "Tom", "age": 5}
name = "Tom"
tpl = ("n", "a", "g")

result = dct["age"] in lst
print(result)

result = dct["age"] in lst and dct["name"] in tpl
print(result)

check = None

print(dct["name"] == name and dct["age"] in lst)

int = 5
print(type(int))

num_1 = 5
print(type(num_1))

num_2 = 3.14
print(type(num_2))

string = "hello"
print(type(string))

check = True
print(type(check))

lst = ["hello", "my", "name", "is", "Tom"]
print(type(lst))

tpl = (1, 2, 3)
print(type(tpl))

dct = {"name": "John", "age": 23}
print(type(dct))

set_ex = {1, 2, 3}
print(type(set_ex))

none_var = None
print(type(none_var))

class Person:
    pass

a = Person()
print(type(a))
num_1 = 100
num_2 = 10

num_3 = num_1 + num_2
print(num_3)

num_3 = num_1 - num_2
print(num_3)

num_3 = num_1 * num_2
print(num_3)

num_3 = num_1 / num_2
print(num_3)

num_1 = 7
num_2 = 2

num_3 = num_1 / num_2
num_4 = num_1 // num_2
print(num_3, num_4)

num_1 = 5
num_2 = 2

num_3 = num_1 ** num_2
print(num_3)

num_1 = 7
num_2 = 2

num_3 = num_1 % num_2
print(num_3)

num_1 = 10
num_2 = 3

num_3 = num_1 % num_2
print(num_3)

num_1 = 10
num_2 = 5

num_3 = num_1 == num_2
print(num_3)

num_3 = num_1 != num_2
print(num_3)

num_3 = num_1 < num_2
print(num_3)

num_3 = num_1 > num_2
print(num_3)

num = 10
name = "Tom"

result = num > 5 and name == "Tom"
print(result)

result = num < 5 or name == "Tom"
print(result)

result = num < 5 and name == "Tom"
print(result)

message = "Tom get some money"
print(name in message)
print(name not in message)

name = "John"
message = "You won!"
print(name in message)
print(name not in message)

age = 50
name = "Ira"
animal = "Cat"

print(age == 50 and "Ira" in name and animal != "dog")
print(age == 50 and "I" in name or animal == "dog")
print(age == 50 and "F" in name and animal != "dog")
reserve_words = """
    False     await     else      import    pass
    None      break     except    in        raise
    True      class     finally   is        return
    and       continue  for       lambda    try
    as        def       from      nonlocal  while
    assert    del       global    not       with
    async     elif      if        or        yield
"""

name = "Tom"
Name = "Tom"
print(name, Name)

user_email = "example@gmail.com"
userEmail = "example@gmail.com"
print(user_email, userEmail)

name = "Jon"
print(name)
name = "Tom"
print(name)