import re

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

splitted_by_h = adwentures_of_tom_sawer.split("h")
count_h = len(splitted_by_h) - 1
print("у тексті літера h зустрічається", count_h, "разів")

#or can be done using re

find_all_h = re.findall("h", adwentures_of_tom_sawer)
count_h_re = len(find_all_h)
print(count_h_re, "разів у тексті зустрічається літера h")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

find_capital_letters = re.findall("[A-Z]", adwentures_of_tom_sawer)
count_capital_letters = len(find_capital_letters)
print(count_capital_letters, "слів у тексті починається з Великої літери")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

split_by_tom = adwentures_of_tom_sawer.split('Tom')
print(adwentures_of_tom_sawer.find(split_by_tom[2]) - 3, "слово Tom зустрічається вдруге")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

splitted_by_end_sentence = adwentures_of_tom_sawer.split(".")
adwentures_of_tom_sawer_sentences = len(splitted_by_end_sentence) - 1
#print(splitted_by_end_sentence)
print(adwentures_of_tom_sawer_sentences, "- це кількість речень в тексті")

#Counting by dots as the end of a sentence
count_dots = re.findall("\.", adwentures_of_tom_sawer)
number_of_dots = len(count_dots)
print(number_of_dots, "- це кількість речень в тексті")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

splitted_by_end_sentence_new = adwentures_of_tom_sawer.split(".")
fourth_sentence = splitted_by_end_sentence_new[3]
print(fourth_sentence,'- це четверте речення')

fourth_sentence_lower = fourth_sentence.lower()
print(fourth_sentence_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

check_sentence_starts = adwentures_of_tom_sawer.find("By the time")
if check_sentence_starts != -1:
    print(f"Так, якесь речення починається з 'By the time'")
else:
    print("Підстрочка не знайдена.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = splitted_by_end_sentence_new[-2]
words_last_sentence = last_sentence.split()
count_words_last_sentence = len(words_last_sentence)
print(count_words_last_sentence)

#count_words_last_sentence = len(splitted_by_end_sentence_new[-2].split())
#print(count_words_last_sentence)
