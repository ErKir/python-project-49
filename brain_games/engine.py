import prompt

# number of game rounds
number_of_rounds = 3


def game_engine(rules, round):
    greeting = 'Welcome to the Brain Games!'
    print(greeting)
    name = prompt.string('May I have your name?\n')
    print(f'Hello, {name}!')
    print(rules)
    round_of_game = 1
    while round_of_game <= number_of_rounds:
        round_of_game += 1
        round_data = round()
        (question, correct_answer) = round_data
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
