from brain_games.random_numb import get_random_num
from brain_games.engine import game_engine


# the range for random number generator (use int)
min_start = 1
max_start = 10
min_step = 1
max_step = 10
min_length_progression = 5
max_length_progression = 10


rules_of_game = 'What number is missing in the progression?'


def get_progression():
    start = get_random_num(min_start, max_start)
    length_progression = get_random_num(
        min_length_progression, max_length_progression)
    step = get_random_num(min_step, max_step)
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
    return game_engine(rules_of_game, round)
