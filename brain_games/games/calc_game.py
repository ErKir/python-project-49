import random

# the range for random number generator (use int)
MIN_NUMBER = 1
MAX_NUMBER = 20

# math OPERATIONS
OPERATIONS = ['-', '+', '*']


RULES_OF_GAME = 'What is the result of the expression?'


def get_random_num(min_number, max_number):
    return random.randint(min_number, max_number)


def round():
    numb1 = get_random_num(MIN_NUMBER, MAX_NUMBER)
    numb2 = get_random_num(MIN_NUMBER, MAX_NUMBER)
    operation = OPERATIONS[get_random_num(0, 2)]
    question = f'{numb1} {operation} {numb2}'
    answer = eval(question)
    return (question, str(answer))


def game():
    return (RULES_OF_GAME, round)
