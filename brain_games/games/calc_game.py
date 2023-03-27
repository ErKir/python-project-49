from brain_games.random_numb import get_random_num
from brain_games.engine import game_engine


# the range for random number generator (use int)
min_number = 1
max_number = 20

# math operations
operations = ['-', '+', '*']


rules_of_game = 'What is the result of the expression?'


def round():
    numb1 = get_random_num(min_number, max_number)
    numb2 = get_random_num(min_number, max_number)
    operation = operations[get_random_num(0, 2)]
    question = f'{numb1} {operation} {numb2}'
    answer = eval(question)
    return (question, str(answer))


def game():
    return game_engine(rules_of_game, round)
