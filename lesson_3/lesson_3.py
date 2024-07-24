print('\n'
      '***\n'
      'Задачі №1-3\n')
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n"'
                       '—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print('\n'
      '***\n'
      'Задача №4\n')

area_black_sea = 436402
area_azov_sea = 37800

general_sea_area = area_black_sea + area_azov_sea

print('Чорне та Азовське моря разом займають:', general_sea_area, 'км2')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

print('\n'
      '***\n'
      'Задача №5\n')

sum_general_storage = 375291
sum_first_second_storage = 250449
sum_second_third_storage = 222950

sum_first_storage = sum_general_storage - sum_second_third_storage
sum_second_storage = sum_first_second_storage - sum_first_storage
sum_third_storage = sum_second_third_storage - sum_second_storage

print('на першому складі', sum_first_storage, 'товарів \n'
      'на другому складі', sum_second_storage, 'товарів \n'
      'на третьому складі', sum_third_storage, 'товарів')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('\n'
      '***\n'
      'Задача №6\n')

credit_lasts = 16
credit_month_payment = 1179

computer_price = credit_month_payment * credit_lasts

print('Вартість комп’ютера', computer_price)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# THIS TASK WAS DONE IN A SUCH WAY JUST FOR PRACTICING TUPLES. IT COULD BE DONE MUCH EASIER
print('\n'
      '***\n'
      'Задача №7\n')

remainder_division = [8019 % 8, 9907 % 9, 2789 % 5, 7248 % 6, 7128 % 5, 19224 % 9]
first_remainder = remainder_division[0]
second_remainder = remainder_division[1]
third_remainder = remainder_division[2]
fourth_remainder = remainder_division[3]
fifth_remainder = remainder_division[4]
sixth_remainder = remainder_division[5]
print('перша остача від ділення =', first_remainder)
print('друга остача від ділення =', second_remainder)
print('третя остача від ділення =', third_remainder)
print('четверта остача від ділення =', fourth_remainder)
print('п\'ята остача від ділення =', fifth_remainder)
print('шоста остача від ділення =', sixth_remainder)

# task 08
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

print('\n'
      '***\n'
      'Задача №8\n')

# Prices

price_pizza_big = 274
price_pizza_medium = 218
price_juice = 35
price_cake = 350
price_water = 21


# Counts of items

count_pizza_big = 4
count_pizza_medium = 2
count_juice = 4
count_cake = 1
count_water = 3

# General price

pay_for_order = (price_pizza_big * count_pizza_big
                 + price_pizza_medium * count_pizza_medium
                 + price_juice * count_juice
                 + price_cake * count_cake
                 + price_water * count_water)

print('Для даного замовлення Іринці знадобиться:', pay_for_order, 'грн')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print('\n'
      '***\n'
      'Задача №9\n')

count_all_photos = 232
count_one_page_photos = 8
count_pages = count_all_photos // count_one_page_photos

print('знадобиться:', count_pages, 'сторінок')


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

print('\n'
      '***\n'
      'Задача №10\n')

distance_journey = 1600
fuel_economy = 9 / 100
tank_capacity = 48

fuel_needed = distance_journey * fuel_economy
distance_one_tank_to_empty = tank_capacity / fuel_economy
times_to_stop = int(distance_journey / distance_one_tank_to_empty)

print(fuel_needed, 'літрів бензину знадобиться для подорожі')
print(times_to_stop, 'разів необхідно заїхати на заправку під час подорожі')
