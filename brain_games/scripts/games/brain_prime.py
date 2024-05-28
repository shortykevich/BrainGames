#!/usr/bin/env python3
import os

from brain_games.scripts.games import (
    ROUNDS_PER_GAME,
    greeting,
    generate_argument,
    calculate_right_answer,
    ask_question_and_get_answer,
    is_wrong_answer,
    specify_instructions
)


def main():
    name = greeting()
    game_name = specify_instructions(os.path.basename(__file__))

    for i in range(ROUNDS_PER_GAME):
        random_value = generate_argument(game_name)
        correct_answer = calculate_right_answer(game_name, random_value)
        answer = ask_question_and_get_answer(game_name, random_value)

        if is_wrong_answer(answer, correct_answer, name):
            return None

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
