# ==========================
# 1. Рядки (Strings)
# ==========================

# Функція приймає рядок і повертає його довжину
def string_length(text):
    return len(text)


# Функція приймає два рядки і повертає об'єднаний рядок
def join_strings(text1, text2):
    return text1 + text2


# ==========================
# 2. Числа (Int/float)
# ==========================

# Функція повертає квадрат числа
def square(number):
    return number ** 2


# Функція повертає суму двох чисел
def add_numbers(num1, num2):
    return num1 + num2


# Функція повертає цілу частину від ділення та залишок
def divide_numbers(num1, num2):
    return num1 // num2, num1 % num2


# ==========================
# 3. Списки (Lists)
# ==========================

# Функція обчислює середнє значення списку чисел
def average(numbers):
    return sum(numbers) / len(numbers)


# Функція повертає список спільних елементів двох списків
def common_elements(list1, list2):
    return list(set(list1) & set(list2))


# ==========================
# 4. Словники (Dictionaries)
# ==========================

# Функція виводить всі ключі словника
def print_keys(dictionary):
    for key in dictionary:
        print(key)


# Функція об'єднує два словники
def merge_dictionaries(dict1, dict2):
    return dict1 | dict2


# ==========================
# 5. Множини (Sets)
# ==========================

# Функція повертає об'єднання двох множин
def union_sets(set1, set2):
    return set1 | set2


# Функція перевіряє, чи є одна множина підмножиною іншої
def is_subset(set1, set2):
    return set1.issubset(set2)


# ==========================
# 6. Умовні вирази та цикли
# ==========================

# Функція визначає, чи є число парним
def even_or_odd(number):
    if number % 2 == 0:
        return "Парне"
    else:
        return "Непарне"


# Функція повертає список тільки з парними числами
def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


# ==========================
# 7. Лямбда-функція
# ==========================

# Лямбда-функція визначає парне чи непарне число
check_even = lambda number: "Парне" if number % 2 == 0 else "Не парне"


# ==========================
# Приклади використання
# ==========================

print(string_length("Python"))
print(join_strings("Hello, ", "World!"))

print(square(5))
print(add_numbers(10, 15))
print(divide_numbers(17, 5))

print(average([10, 20, 30, 40]))
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))

print_keys({"name": "Alex", "age": 25})

print(merge_dictionaries({"a": 1}, {"b": 2}))

print(union_sets({1, 2, 3}, {3, 4, 5}))
print(is_subset({1, 2}, {1, 2, 3, 4}))

print(even_or_odd(8))
print(even_numbers([1, 2, 3, 4, 5, 6]))

print(check_even(10))
print(check_even(7))