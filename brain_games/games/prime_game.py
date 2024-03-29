import random

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
            return False
        i += 1
    return True


def get_question_and_answer():
    question_numb = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(question_numb) else 'no'
    return str(question_numb), answer
