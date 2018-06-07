"""
Current state class for poker game. Each state is one rotation - preflop, flop, post-flop, turn, post-turn, river,
post river.
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
        self.current_pot, self.current_bet = 0, 0
        self.active_players = [player for player in self.player_list]

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
        TODO:

        2. Check

        5. Check if you need to pass the move to the next player after the move (change player.position
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
                self.active_players.pop(self.player_list.index(self.get_current_player()))
            # if current player bets/raises: prompt bet/raise amount, add that to the pot, update self.current_bet
            elif move == "Bet" or move == "Raise":
                # ask for amount
                amount = input("Bet or Raise amount: ")
                # deduce the amount from the player's bank
                self.get_current_player().bank -= amount
                # add the amount to the pot
                self.current_pot += amount
                # add the amount to current bet
                self.current_bet += amount
                # update to_call for all the other players
                for player in self.player_list:
                    player.to_call = amount
                # if the player raises, add everyone back to the active_players list except the player
                if move == "Raise":
                    self.active_players = [player for player in self.player_list]
                    self.active_players.pop(self.player_list.index(self.get_current_player()))

            # if player calls: add to the pot.
            elif move == "Call":
                # deduce to_call from the bank
                self.get_current_player().bank -= self.get_current_player().to_call
                # add to_call to the pot
                self.current_pot += self.get_current_player().to_call
                # remove the player from the active_player list
                self.active_players.pop(self.player_list.index(self.get_current_player()))
            elif move == "Check":
                self.active_players.pop(self.player_list.index(self.get_current_player()))
            # Create a new state
            new_state = CurrentState(self.small_blind, self.player_list)
            return new_state



