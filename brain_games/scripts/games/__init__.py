import prompt
from math import gcd, sqrt

from brain_games import welcome_user
from random import randint, choice
from brain_games.scripts.games.constants import (
    ROUNDS_PER_GAME,
    START_INT,
    END_INT,
    PROGRESSION_LEN_INTERVAL,
    PROGRESSION_STEP_INTERVAL,
)


def greeting() -> str:
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def specify_instructions(game_name: str) -> None:
    match game_name:
        case 'brain-calc':
            print('What is the result of the expression?')

        case 'brain-even':
            print('Answer "yes" if the number is even, '
                  'otherwise answer "no".')

        case 'brain-gcd':
            print('Find the greatest common divisor of given numbers.')

        case 'brain-prime':
            print('Answer "yes" if given number is prime. '
                  'Otherwise answer "no".')

        case 'brain-progression':
            print('What number is missing in the progression?')
    return None


def start_game(game_name: str) -> bool:
    specify_instructions(game_name)
    for i in range(ROUNDS_PER_GAME):
        random_value = generate_argument(game_name)
        correct_answer = calculate_right_answer(game_name, random_value)
        answer = ask_question_and_get_answer(game_name, random_value)
        if is_wrong_answer(answer, correct_answer):
            return False
    return True


def finish_game(result: bool, name: str) -> None:
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")
    return None


def play_game(game_name: str) -> None:
    name = greeting()
    result = start_game(game_name)
    finish_game(result, name)


def generate_argument(script_name: str) -> int | tuple:
    match script_name:
        case 'brain-even':
            return randint(START_INT, END_INT)

        case 'brain-calc':
            rand_math_expression = choice(['+', '-', '*'])
            rand_value1 = randint(START_INT, END_INT)
            rand_value2 = randint(START_INT, END_INT)
            return rand_value1, rand_value2, rand_math_expression

        case 'brain-gcd':
            return (randint(START_INT, END_INT),
                    randint(START_INT, END_INT))

        case 'brain-progression':
            start_point = randint(START_INT, END_INT)

            x1, x2 = PROGRESSION_LEN_INTERVAL
            progression_length = randint(x1, x2)

            min_s, max_s = PROGRESSION_STEP_INTERVAL
            step = 0
            while not step:
                step = randint(min_s, max_s)

            hidden_position = randint(0, progression_length - 1)

            hidden_value = 0
            progression = []
            for i in range(progression_length):
                member = start_point + (i + 1) * step
                if i == hidden_position:
                    hidden_value = member
                    progression.append('..')
                else:
                    progression.append(str(member))

            return hidden_value, ' '.join(progression)

        case 'brain-prime':
            return randint(START_INT, END_INT)


def calculate_right_answer(script_name: str,
                           source: int | tuple
                           ) -> int | tuple | str:
    match script_name:
        case 'brain-even':
            return 'yes' if source % 2 == 0 else 'no'

        case 'brain-calc':
            a, b, expression = source
            return str(a + b) if expression == '+' else (
                str(a - b) if expression == '-' else str(a * b))

        case 'brain-gcd':
            a, b = source
            return str(gcd(a, b))

        case 'brain-progression':
            correct_answer, _ = source
            return str(correct_answer)

        case 'brain-prime':
            return 'yes' if is_prime(source) else 'no'


def ask_question_and_get_answer(script_name: str,
                                source: int | tuple
                                ) -> str:
    question = ''
    match script_name:
        case 'brain-even' | 'brain-prime':
            question = f'{source}'

        case 'brain-calc':
            a, b, expression = source
            question = f'{a} {expression} {b}'

        case 'brain-gcd':
            a, b = source
            question = f'{a} {b}'

        case 'brain-progression':
            _, progression = source
            question = f'{progression}'

    print(f'Question: {question}')
    return prompt.string("Your answer: ")


def is_wrong_answer(answer: int | str,
                    correct_answer: str,
                    ) -> bool:
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        return True
    return False


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    end_of_range = int(sqrt(num)) + 1
    for i in range(2, end_of_range):
        if num % i == 0:
            return False
        i += 6
    return True


__all__ = [
    'ROUNDS_PER_GAME',
    'specify_instructions',
    'start_game',
    'finish_game',
    'greeting',
    'generate_argument',
    'calculate_right_answer',
    'ask_question_and_get_answer',
    'is_wrong_answer',
    'play_game'
]
