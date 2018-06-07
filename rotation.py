"""
Current rotation class for poker game. Each rotation is one rotation - preflop, flop, post-flop, turn, post-turn, river,
post river.
"""
from game import Player


class Rotation:
    """
    Current rotation class
    """

    def __init__(self, small_blind: int, player_list: list) -> None:
        """
        Initializes a new rotation in a poker game.
        starting_amount is the starting bank for each player,
        small_blind is the small blind amount
        """
        self.small_blind, self.player_list = small_blind, player_list
        self.current_pot, self.current_bet = 0, 0
        self.active_players = [player for player in self.player_list]
        self.rotation_number = 0

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
        for player in self.active_players:
            if player.is_turn:
                return player

    def get_next_player(self) -> "Player":
        """
        Returns the next player
        """
        return self.active_players[self.player_list.index(self.get_current_player()) + 1]

    def get_prev_player(self) -> "Player":
        """
        Returns the previous player
        """
        return self.active_players[self.player_list.index(self.get_current_player()) - 1]


    def get_possible_moves(self) -> list:
        """
        Returns a string containing possible moves
        """
        # if the player does not have to call, the player can check or raise/bet or fold
        if self.get_current_player().to_call == 0:
            possible_moves = ["Fold", "Raise", "Check"]

            # if it's post-flop, change Raise to Bet
            if self.rotation_number != 0:
                possible_moves[1] = "Bet"

        else:
            possible_moves = ["Fold", "Raise", "Call"]
        return possible_moves



    def is_valid_move(self, move) -> bool:
        """
        Returns whether or not the selected move is valid
        """
        valid_move = False
        if move in self.get_possible_moves():
            valid_move = True
        return valid_move

    def rotation_over(self) -> bool:
        """
        Returns whether or not the current rotation is over
        """
        rotation_over = False
        truth_list = [True if player.to_call == 0 else False for player in self.active_players]
        # If everyone called or everyone checked (to_call is zero)
        if all(truth_list):
            rotation_over = True
            self.rotation_number += 1
        return rotation_over

    def make_move(self, move: str):
        """
        Applies the move.
        """
        # Check if the player's bank == 0 (allin or bankrupt):
        if self.get_current_player().bank == 0:
            # Update the flags before prompting a move to skip a turn
            self.get_current_player().is_turn = False
            self.get_next_player().is_turn = True
        else:
            if not self.is_valid_move(move):
                raise ValueError('The selected move is not valid')
            else:

                # if current player folds, remove the player from the list of players
                if move == "Fold":
                    self.player_list.pop(self.player_list.index(self.get_current_player()))
                    self.active_players.pop(self.player_list.index(self.get_current_player()))

                # if current player bets/raises: prompt bet/raise amount, add that to the pot, update self.current_bet
                elif move == "Bet" or move == "Raise":
                    # ask for amount
                    amount = int(input("Bet or Raise amount: "))
                    # checks if the raise amount is present in the player's bank, prompts again otherwise
                    while not amount > self.get_current_player().bank:
                        # ask for amount
                        amount = int(input("Bet or Raise amount: "))
                    # deduce the amount from the player's bank
                    self.get_current_player().bank -= (self.get_current_player().to_call + amount)
                    # add the amount to the pot
                    self.current_pot += (self.get_current_player().to_call + amount)
                    # add the amount to current bet
                    self.current_bet += (self.get_current_player().to_call + amount)
                    # update to_call for all the other players
                    for player in self.player_list:
                        player.to_call = (player.to_call + amount)
                    # if the player raises, add everyone back to the active_players list except the player
                    if move == "Raise":
                        self.active_players = [player for player in self.player_list]
                        self.active_players.pop(self.player_list.index(self.get_current_player()))

                # if player calls: add to the pot.
                elif move == "Call":
                    # if to_call is >= the player's bank, the player is allin
                    if self.get_current_player().bank > self.get_current_player().to_call:
                        # deduce to_call from the bank
                        self.get_current_player().bank -= self.get_current_player().to_call
                        # add to_call to the pot
                        self.current_pot += self.get_current_player().to_call
                    else:
                        self.current_pot += self.get_current_player().bank
                        self.get_current_player().bank = 0
                    # remove the player from the active_player list
                    self.get_current_player().to_call = 0
                    self.active_players.pop(self.player_list.index(self.get_current_player()))

                elif move == "Check":
                    self.active_players.pop(self.player_list.index(self.get_current_player()))

                # Update the flags
                self.get_current_player().is_turn = False
                self.get_next_player().is_turn = True

            # Create a new rotation
            new_rotation = Rotation(self.small_blind, self.player_list)
            return new_rotation



