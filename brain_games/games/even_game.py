import random

# the range for random number generator (use int)
MIN_NUMBER = 1
MAX_NUMBER = 100

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random_num(min_number, max_number):
    return random.randint(min_number, max_number)


def is_even(num):
    return 'yes' if (num % 2 == 0) else 'no'


def round():
    question_numb = get_random_num(MIN_NUMBER, MAX_NUMBER)
    answer = is_even(question_numb)
    return (question_numb, answer)


def game():
    return (RULES_OF_GAME, round)
