# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_digits(d_1, d_2):
    return d_1 + d_2

digit_1 = 5
digit_2 = 7

# dodigit_1 = 10
# dodigit_2 = 4

print('сума двох чисел:', sum_two_digits(digit_1, digit_2))
# print(sum_two_digits(digit_1, sum_two_digits(dodigit_1, dodigit_2)))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average(digits_for_average):
    if not digits_for_average:
        return 0
    return sum(digits_for_average) / len(digits_for_average)

averadge_digits_list_1 = []
averadge_digits_list_2 = [101, 275, 3777, 754, 15, 336, 6859, 935967, 1, 55]
averadge_digits_list_3 = [10, 20, 30, 40, 50, 60]
average = calculate_average(averadge_digits_list_3)
print(f"Середнє арифметичне: {average}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_direction(str_raw):
    str_reverse = ''
    str_len = len(str_raw)
    for i in reversed(range(str_len)):
        str_reverse = str_reverse + str_raw[i]
    return str_reverse

str_to_reverse_1 = "refrigerator"
reverse = reverse_direction(str_to_reverse_1)
print(reverse)



# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def the_longest_word_f(list_of_words):
    max_length_word = ''
    for word in list_of_words:
        if len(word) >= len(max_length_word):
            max_length_word = word
    return max_length_word

list_of_words_example_1 = ('apple', 'banana', 'pineapple', 'coconut')

the_longest_word = the_longest_word_f(list_of_words_example_1)
print(the_longest_word)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 was created by myself
# To write a function(s) which takes the biggest value from each list and then sum them

def sum_two_biggest_values_1(list_of_values_task_7):
    max_element = 0
    for element in list_of_values_task_7:
        if element >= max_element:
            max_element = element
    return max_element

def get_sum(a, b):
    return (a + b)

some_list_1 = [1, 2, 3, 4, 9, 3]
some_list_2 = [100, 1]

sum_two_values = get_sum(sum_two_biggest_values_1(some_list_1), sum_two_biggest_values_1(some_list_2))
print(sum_two_values)


# task 8 was created by myself
# Here is the list of countries which participate in Olympic games. Write a function which order countries by places.
# Ordering should be by number of gold medals, than by silver medals, than by bronze medals
# Should print: Country: Gold number of medals, Silver number of medals, Bronze number of medals

def sort_countries_by_medals(countries_medals):
    # Sorting by gold, silver, bronze
    sorted_countries = sorted(countries_medals, key=lambda x: (-x[1], -x[2], -x[3]))

    for country in sorted_countries:
        print(f"{country[0]}: Gold {country[1]}, Silver {country[2]}, Bronze {country[3]}")

# The list of countries
countries_medals = [
    ("USA", 39, 41, 33),
    ("Canada", 19, 32, 18),
    ("Japan", 27, 14, 17),
    ("Great Britain", 22, 21, 22),
    ("Ukraine", 8, 9, 18),
    ("Poland", 8, 7, 20),
    ("France", 10, 10, 25),
    ("Germany", 10, 10, 24),
]

sort_countries_by_medals(countries_medals)

# task 9
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

def order_sum(order_items, prices):
    return sum(quantity * price for quantity, price in zip(order_items, prices))

# Prices
prices = {
    'pizza_big': 274,
    'pizza_medium': 218,
    'juice': 35,
    'cake': 350,
    'water': 21
}

order_items = [
    int(input("How many big pizzas? ")),
    int(input("How many medium pizzas? ")),
    int(input("How much juice? ")),
    int(input("How many cakes? ")),
    int(input("How much water? "))
]

# General price
general_price_of_order = order_sum(order_items, list(prices.values()))

print(f"General price: {general_price_of_order}")

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def credit_payment(credit_conditions):
    monthly_payment, months = credit_conditions
    return monthly_payment * months

credit_conditions = [
    int(input("How much do you need to pay per month? ")),
    int(input("How many months will you pay? "))
]

total_cost = credit_payment(credit_conditions)
print(f"Total cost of the computer: {total_cost} UAH")
