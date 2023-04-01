import random
import operator
# the range for random number generator (use int)
MIN_NUMBER = 1
MAX_NUMBER = 20

# math OPERATIONS
OPERATIONS = ['-', '+', '*']
ACTION = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

RULES_OF_GAME = 'What is the result of the expression?'


def get_question_and_answer():
    numb1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    numb2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = OPERATIONS[random.randint(0, 2)]
    question = f'{numb1} {operation} {numb2}'
    answer = str(ACTION[operation](numb1, numb2))
    return question, answer
