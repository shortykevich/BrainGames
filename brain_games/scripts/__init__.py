from brain_games.scripts.brain_games import main
from brain_games import welcome_user


def greeting():
    print('Welcome to the Brain Games!')
    return welcome_user()


__all__ = [
    'main',
    'greeting'
]
