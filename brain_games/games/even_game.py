import random

# the range for random number generator (use int)
MIN_NUMBER = 1
MAX_NUMBER = 100

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question_and_answer():
    question_numb = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_even(question_numb) else 'no'
    return question_numb, answer
