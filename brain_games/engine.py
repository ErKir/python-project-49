import prompt
# number of game rounds
NUMBER_OF_ROUNDS = 3


def game_engine(game_module):
    greeting = 'Welcome to the Brain Games!'
    print(greeting)
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')
    print(game_module.RULES_OF_GAME)
    round_of_game = 1
    while round_of_game <= NUMBER_OF_ROUNDS:
        round_of_game += 1
        question, correct_answer = game_module.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if (user_answer == correct_answer):
            print('Correct!')
        else:
            print(
                f'{user_answer} is wrong answer ;(. Correct answer was '
                f'{correct_answer}.\nLet\'s try again, {name}!'
            )
            return
    print(f'Congratulations, {name}!')
