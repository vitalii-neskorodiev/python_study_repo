#Task 8.1

test_list_1: list[str] = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
test_list_2: list[str] = ["1,2,3,4", "1,2,3,4,50"]

def sum_all_chars_in_string_if_int(test_list: list[str]) -> None:
    result: list[int] = list()
    try:
        for item in test_list:
            chars_list: list = item.split(",")
            result.append(sum(int(integer) for integer in chars_list))
    except ValueError as exception:
        print(f"I cannot sum your items from list due to: {exception}")
    else:
        print(result)

sum_all_chars_in_string_if_int(test_list_2)
