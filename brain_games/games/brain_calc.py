#!/usr/bin/env python3
import os

from brain_games.games import (
    ROUNDS_IN_GAME, greeting,
    generate_argument,
    calculate_right_answers,
    ask_question_and_get_answer,
    is_wrong_answer
)


def main():
    name = greeting()
    script_name = os.path.basename(__file__)
    print('What is the result of the expression?')

    for i in range(ROUNDS_IN_GAME):
        random_value = generate_argument(script_name)
        correct_answer = calculate_right_answers(script_name, random_value)
        answer = ask_question_and_get_answer(random_value)

        if is_wrong_answer(answer, correct_answer, name):
            return None

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
