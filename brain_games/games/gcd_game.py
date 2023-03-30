import random

# the range for random number generator (use int)
MIN_NUMBER = 1
MAX_NUMBER = 100

RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def get_random_num(min_number, max_number):
    return random.randint(min_number, max_number)


def get_gcd(num1, num2):
    if (not num2):
        return num1
    return get_gcd(num2, num1 % num2)


def round():
    numb1 = get_random_num(MIN_NUMBER, MAX_NUMBER)
    numb2 = get_random_num(MIN_NUMBER, MAX_NUMBER)
    question = f'{numb1} {numb2}'
    answer = get_gcd(numb1, numb2)
    return (question, str(answer))


def game():
    return (RULES_OF_GAME, round)
