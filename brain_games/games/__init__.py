import prompt
from math import gcd

from brain_games import welcome_user
from random import randint, choice

ROUNDS_IN_GAME = 3


def greeting():
    print('Welcome to the Brain Games!')
    return welcome_user()


def generate_argument(script_name):
    match script_name:
        case 'brain_even.py':
            return randint(1, 100)

        case 'brain_calc.py':
            rand_math_expression = choice(['+', '-', '*'])
            rand_value1 = randint(1, 100)
            rand_value2 = randint(1, 100)
            return rand_value1, rand_value2, rand_math_expression

        case 'brain_gcd.py':
            return randint(1, 100), randint(1, 100)

        case _:
            return None


def calculate_right_answers(script_name, source):
    match script_name:
        case 'brain_even.py':
            return 'yes' if source % 2 == 0 else 'no'

        case 'brain_calc.py':
            a, b, expression = source
            return str(a + b) if expression == '+' else (
                str(a - b) if expression == '-' else str(a * b))

        case 'brain_gcd.py':
            a, b = source
            return str(gcd(a, b))

        case _:
            return None


def ask_question_and_get_answer(source):
    if isinstance(source, tuple):
        if len(source) > 2:
            a, b, expression = source
            print(f"Question: {a} {expression} {b}")
        else:
            a, b = source
            print(f"Question: {a} {b}")
    elif isinstance(source, int):
        print(f"Question: {source}")
    elif isinstance(source, list):
        pass

    return prompt.string("Your answer: ")


def is_wrong_answer(answer, correct_answer, name):
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}")
        return True


__all__ = [
    'ROUNDS_IN_GAME',
    'greeting',
    'generate_argument',
    'calculate_right_answers',
    'ask_question_and_get_answer',
    'is_wrong_answer',

]
