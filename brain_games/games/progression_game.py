import random

# the range for random number generator (use int)
MIN_START = 1
MAX_START = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH_PROGRESSION = 5
MAX_LENGTH_PROGRESSION = 10


RULES_OF_GAME = 'What number is missing in the progression?'


def get_random_num(min_number, max_number):
    return random.randint(min_number, max_number)


def get_progression():
    start = get_random_num(MIN_START, MAX_START)
    length_progression = get_random_num(
        MIN_LENGTH_PROGRESSION, MAX_LENGTH_PROGRESSION)
    step = get_random_num(MIN_STEP, MAX_STEP)
    progression = [start, ]
    current = start
    while length_progression:
        current += step
        progression.append(current)
        length_progression -= 1
    return progression


def round():
    progression = get_progression()
    random_index = get_random_num(0, len(progression) - 1)
    answer = progression[random_index]
    progression[random_index] = '..'
    string_progression = [str(el) for el in progression]
    question = ' '.join(string_progression)
    return (question, str(answer))


def game():
    return (RULES_OF_GAME, round)
