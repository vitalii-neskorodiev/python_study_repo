#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(number_finish):
    return (num for num in range(0, number_finish + 1, 2))


last_number: int = 23
even_gen = even_numbers(last_number)
for even in even_gen:
    print(even)


#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_sequence(fibonacci_limit):
    fibs = [0, 1]
    while fibs[-1] + fibs[-2] <= fibonacci_limit:
        fibs.append(fibs[-1] + fibs[-2])
    return (num for num in fibs)


fibonacci_last_num: int = 99
fib_gen = fibonacci_sequence(fibonacci_last_num)
for fib in fib_gen:
    print(fib)


#Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


example_list: list = [1, 2, 3, 4, 5]
reverse_iter = ReverseIterator(example_list)
for item in reverse_iter:
    print(item)


#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbersIterator:
    def __init__(self, last_num):
        self.last_num = last_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.last_num:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


last_number_iterator = 15
even_iter = EvenNumbersIterator(last_number_iterator)
for even in even_iter:
    print(even)


#Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@log_arguments_and_result
def add(a, b):
    return a + b


add(8, 11)


#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught: {e}")
    return wrapper


@catch_exceptions
def divide(x, y):
    return x / y


divide(10, 2)
divide(10, 0)
