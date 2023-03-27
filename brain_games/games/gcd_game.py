from brain_games.random_numb import get_random_num
from brain_games.engine import game_engine


# the range for random number generator (use int)
min_number = 1
max_number = 100

rules_of_game = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    if (not num2):
        return num1
    return get_gcd(num2, num1 % num2)


def round():
    numb1 = get_random_num(min_number, max_number)
    numb2 = get_random_num(min_number, max_number)
    question = f'{numb1} {numb2}'
    answer = get_gcd(numb1, numb2)
    return (question, str(answer))


def game():
    return game_engine(rules_of_game, round)
