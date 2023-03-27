from brain_games.random_numb import get_random_num


# the range for random number generator (use int)
# minimum number is 2, because
# a prime number is a natural number greater than 1!
MIN_NUMBER = 2
MAX_NUMBER = 100

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    question_numb = get_random_num(MIN_NUMBER, MAX_NUMBER)
    answer = is_prime(question_numb)
    return (str(question_numb), answer)


def game():
    return (RULES_OF_GAME, round)
