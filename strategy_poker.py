"""
Strategy implementation
"""
from typing import Any  # ,Union
from random import *


def interactive_strategy() -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return move


def random_strategy(game: Any) -> Any:
    """
    Returns a random move
    """
    pass


def ai_strategy() -> Any:
    """
    AI strategy implementation
    """
    pass
