# Task 6.1

proposed_string: str = input("Provide your string here please: ")

unique_counter: int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])

if unique_counter > 10:
    print(True)
else:
    print(False)

#print(unique_counter)


# Task 6.2

is_correct_str: bool = False

while not is_correct_str:
    provided_word: str = input("Provide your word please: ")

    if provided_word.find("h") != -1 or provided_word.find("H") != -1:
        is_correct_str = True


# Task 6.3

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

desired_list: list[str] = [item for item in lst1 if isinstance(item, str)]

#for item in lst1:
#    if isinstance(item, str):
#        desired_list.append(item)

print(desired_list)


# Task 6.4

provided_list_1: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
provided_list_2: list[int] = [10, 11, 20, 27, 30, 33]

result: int = sum([integer for integer in provided_list_1 if integer % 2 == 0])

sum_result: int = 0
for integer in provided_list_2:
    if integer % 2 == 0:
        sum_result += integer

print(sum_result)
print(result)
