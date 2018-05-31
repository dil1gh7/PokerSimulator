"""
A NL Texas Hold'Em Poker game.
"""
from current_state_poker import *


class Poker:
    """
    ...
    """
    def __init__(self, starting_amount, small_blind, number_of_players):
        """
        Initializes a new poker game, asks for the starting bank, the small
        blind amount and the amount of players. Sets big_blind = 2 * small_blind. Initializes a new state.
        """
        self.player_list = [Player("Player" + str(i + 1)) for i in range(number_of_players)]
        self.starting_amount, self.small_blind, self.big_blind = starting_amount, small_blind, small_blind * 2


    def game_over(self, current_state: CurrentState) -> bool:
        """
        Returns whether or not the tournament is over
        """
        game_over = False
        if len(current_state.player_list) == 1:
            game_over = True
        return game_over

    def game_winner(self) -> Player:
        """
        Returns the winner of the tournament
        """
        assert self.game_over(), 'Game is not over!'
        return self.current_state.player_list[0]

    def current_leaderboards(self) -> str:
        """
        Returns current leaderboard
        """
        pass
