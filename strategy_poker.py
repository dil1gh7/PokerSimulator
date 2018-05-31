"""
Strategy implementation
"""
from typing import Any  # ,Union
from random import *


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: Any) -> Any:
    """
    Returns a random move
    """
    pass


def ai_strategy(game: Any) -> Any:
    """
    AI strategy implementation
    """
    pass
