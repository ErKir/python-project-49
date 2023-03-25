from brain_games.scripts.random_numb import get_random_num
from brain_games.engine import game_engine


# the range for random number generator (use int)
# minimum number is 2, because
# a prime number is a natural number greater than 1!
min_number = 2
max_number = 100

rules_of_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if (num < 2):
        return False
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return 'no'
        i += 1
    return 'yes'


def round():
    question_numb = get_random_num(min_number, max_number)
    answer = is_prime(question_numb)
    return (str(question_numb), answer)


def game():
    return game_engine(rules_of_game, round)
