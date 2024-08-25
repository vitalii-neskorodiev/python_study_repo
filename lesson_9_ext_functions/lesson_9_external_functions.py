# TASK 1
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""


def credit_payment(credit_conditions):
    monthly_payment, months = credit_conditions
    return monthly_payment * months


# TASK 2
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def calculate_average(digits_for_average):
    if not digits_for_average:
        return 0
    return sum(digits_for_average) / len(digits_for_average)


average_digits_list_3: list = [10, 20, 30, 40, 50, 60]
average = calculate_average(average_digits_list_3)


# TASK 3
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


# TASK 4
# To write a function(s) which takes the biggest value from each list and then sum them


def sum_two_biggest_values_1(list_of_values_task_7):
    max_element = 0
    for element in list_of_values_task_7:
        if element >= max_element:
            max_element = element
    return max_element


def get_sum(max_value_list_1, max_value_list_2):
    return max_value_list_1 + max_value_list_2


some_list_1 = [1, 2, 3, 4, 9, 3]
some_list_2 = [100, 1]
sum_two_values = get_sum(sum_two_biggest_values_1(some_list_1), sum_two_biggest_values_1(some_list_2))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def the_longest_word_f(list_of_words):
    max_length_word = ''
    for word in list_of_words:
        if len(word) >= len(max_length_word):
            max_length_word = word
    return max_length_word


list_of_words_example_1: tuple = ('apple', 'banana', 'pineapple', 'coconut')
the_longest_word = the_longest_word_f(list_of_words_example_1)
print(the_longest_word)
