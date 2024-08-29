# TASK 1
import unittest
from lesson_9_ext_functions.lesson_9_external_functions import credit_payment, calculate_average, average_digits_list_3, \
    reverse_direction, str_to_reverse_1, get_sum, sum_two_biggest_values_1, some_list_1, some_list_2, the_longest_word, \
    list_of_words_example_1


class TestOverallCreditPaymentCheck(unittest.TestCase):
    def test_1_year_payment(self):
        result = credit_payment([1000, 12])
        self.assertEqual(result, 12000)

    def test_2_years_payment(self):
        result = credit_payment([1000, 24])
        self.assertEqual(result, 24000)


# TASK 2

class TestAverageListCheck(unittest.TestCase):
    def test_first_list_of_digits(self):
        result = calculate_average(average_digits_list_3)
        self.assertEqual(result, 35)


# TASK 3


class TestReverseDirectionOfWord(unittest.TestCase):
    def test_reverse_direction_of_word(self):
        result = reverse_direction(str_to_reverse_1)
        self.assertEqual(result, 'rotaregirfer')

    def test_str_to_reverse_contain(self):
        result = str_to_reverse_1
        self.assertTrue('refrigerator')


# TASK 4


class TestTwoBiggestValuesFromTwoLists(unittest.TestCase):

    def test_summ_of_two_biggest_values(self):
        result = get_sum(sum_two_biggest_values_1(some_list_1), sum_two_biggest_values_1(some_list_2))
        self.assertEqual(result, 109)

    def test_list_2_contain(self):
        self.assertIn(100, some_list_2)

    def test_list_2_not_contain(self):
        self.assertNotIn(111, some_list_2)


# TASK 5


class TestLongestWord(unittest.TestCase):

    def test_longest_word(self):
        result = the_longest_word
        self.assertEqual(the_longest_word, 'pineapple')

    def test_list_of_words_contain(self):
        self.assertIn('banana', list_of_words_example_1)


if __name__ == '__main__':
    unittest.main()
