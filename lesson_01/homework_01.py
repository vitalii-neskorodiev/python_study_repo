# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")


# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")


# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)


# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4


# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4


# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples_count = 4
peaches_count = apples_count + 5
plumes_count = apples_count - 2
general_trees_count = apples_count + peaches_count + plumes_count

print(general_trees_count)


# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_before_noon = 0 + 5
temp_afternoon = temp_before_noon - 10
temp_evening = temp_afternoon + 4

print(temp_evening)


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_count = 24
girls_count = boys_count / 2

boys_count_today = boys_count - 1
girls_count_today = girls_count - 2

kids_count_today = boys_count_today + girls_count_today

print(kids_count_today)


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

price_book_1 = 8
price_book_2 = price_book_1 + 2
price_book_3 = (price_book_1 + price_book_2) / 2

summary_price = price_book_1 + price_book_2 + price_book_3

print(summary_price)
