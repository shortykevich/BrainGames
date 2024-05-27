import prompt
from math import gcd, sqrt

from brain_games import welcome_user
from random import randint, choice


ROUNDS_PER_GAME = 3

START_INT = 1
END_INT = 100

PROGRESSION_LEN_INTERVAL = (5, 10)
PROGRESSION_STEP_INTERVAL = (-10, 10)


def greeting() -> str:
    print('Welcome to the Brain Games!')
    return welcome_user()


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    end_of_range = int(sqrt(num)) + 1
    for i in range(2, end_of_range):
        if num % i == 0:
            return False
        i += 6

    return True


def generate_argument(script_name):
    match script_name:
        case 'brain_even.py':
            return randint(START_INT, END_INT)

        case 'brain_calc.py':
            rand_math_expression = choice(['+', '-', '*'])
            rand_value1 = randint(START_INT, END_INT)
            rand_value2 = randint(START_INT, END_INT)
            return rand_value1, rand_value2, rand_math_expression

        case 'brain_gcd.py':
            return (randint(START_INT, END_INT),
                    randint(START_INT, END_INT))

        case 'brain_progression.py':
            start_point = randint(START_INT, END_INT)

            x1, x2 = PROGRESSION_LEN_INTERVAL
            progression_length = randint(x1, x2)

            min_s, max_s = PROGRESSION_STEP_INTERVAL
            step = randint(min_s, max_s)
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

        case 'brain_prime.py':
            return randint(START_INT, END_INT)


def calculate_right_answer(script_name, source):
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

        case 'brain_progression.py':
            correct_answer, _ = source
            return str(correct_answer)

        case 'brain_prime.py':
            return 'yes' if is_prime(source) else 'no'


def ask_question_and_get_answer(script_name, source):
    question = ''
    match script_name:
        case 'brain_even.py' | 'brain_prime.py':
            question = f'{source}'

        case 'brain_calc.py':
            a, b, expression = source
            question = f'{a} {expression} {b}'

        case 'brain_gcd.py':
            a, b = source
            question = f'{a} {b}'

        case 'brain_progression.py':
            _, progression = source
            question = f'{progression}'

    print(f'Question: {question}')
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
    'ROUNDS_PER_GAME',
    'greeting',
    'generate_argument',
    'calculate_right_answer',
    'ask_question_and_get_answer',
    'is_wrong_answer',

]
