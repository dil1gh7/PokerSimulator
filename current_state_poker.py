"""
Current state class for poker game
"""
from player import Player




class CurrentState:
    """
    Current state class
    """

    def __init__(self, small_blind: int, player_list: list) -> None:
        """
        Initializes a new state in a poker game.
        starting_amount is the starting bank for each player,
        small_blind is the small blind amount
        """
        self.small_blind, self.player_list = small_blind, player_list
        self.current_pot = 0

    # def __str__(self):
    #     """
    #     Returns a string representation of self
    #     """
    #     active_players = [i.name for i in self.player_list]
    #     print(active_players)

    def get_current_player(self) -> "Player":
        """
        Returns the name of the current player flagged by player.is_turn == True.
        """
        for player in self.player_list:
            if player.is_turn:
                return player

    def get_next_player(self) -> "Player":
        """
        Returns the next player
        """
        return self.player_list[self.player_list.index(self.get_current_player()) + 1]

    def get_prev_player(self) -> "Player":
        """
        Returns the previous player
        """
        return self.player_list[self.player_list.index(self.get_current_player()) - 1]


    def get_possible_moves(self) -> list:
        """
        Returns a string containing possible moves
        """
        pass

    def is_valid_move(self, move) -> bool:
        """
        Returns whether or not the selected move is valid
        """
        valid_move = False
        if move in self.get_possible_moves():
            valid_move = True
        return valid_move

    def make_move(self, move: str):
        """
        Applies the move
        """
        if not self.is_valid_move(move):
            raise ValueError('The selected move is not valid')
        else:
            # Update the flags
            self.get_current_player().is_turn = False
            self.get_next_player().is_turn = True
            # if current player folds, remove the player from the list of players
            if move == "Fold":
                self.player_list.pop(self.player_list.index(self.get_current_player()))
            # Create a new state
            new_state = CurrentState(self.small_blind, self.player_list)
            return new_state



