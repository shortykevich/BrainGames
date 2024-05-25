#!/usr/bin/env python3
from random import randint
from brain_games.scripts import greeting
import prompt


def main():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        random_number = randint(1, 100)

        right_answer = 'yes' if random_number % 2 == 0 else 'no'

        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")

        if answer == right_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}")
            return None
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
