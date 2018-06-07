"""
A NL Texas Hold'Em Poker game.
"""
from round import Round


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
        self.round = Round(small_blind, self.player_list)
        self.starting_amount, self.small_blind, self.big_blind = starting_amount, small_blind, small_blind * 2

    def game_over(self) -> bool:
        """
        Returns whether or not the game is over
        """
        pass

    def game_winner(self) -> "Player":
        """
        Returns the winner of the tournament
        """
        pass

    def current_leaderboards(self) -> str:
        """
        Returns current leaderboard
        """
        pass


class Player:
    """
    This is a player class.
    Each player has a bank that is updated after each move (unless check).
    Each player has a position that is updated every round.
    Each player has a hand that is updated each round.
    Each player has a current bet that is updated each turn. Need this for bank updates.
    Each player has a to_call value that is updated. Need this for logic.
    Each player has a is_turn bool that is updated each move. Need this to keep track of whose turn it is to move.
    Each player has a name.
    """

    def __init__(self, name: str):
        self.bank = 0
        self.position = 0
        self.hand = []
        self.to_call = 0
        self.is_turn = False
        self.name = name

    def __eq__(self, other) -> bool:
        equal = False
        if self.bank == other.bank:
            equal = True
        return equal

