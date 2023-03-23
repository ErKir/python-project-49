import random
from brain_games.engine import game_engine


# the range for random number generator (use int)
min_number = 1
max_number = 100

rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random_num():
    return random.randint(min_number, max_number)


def is_even(num):
    return 'yes' if (num % 2 == 0) else 'no'


def round():
    question_numb = get_random_num()
    answer = is_even(question_numb)
    return (question_numb, answer)


def game():
    return game_engine(rules_of_game, round)
