# TODO: import the modules needed to make game_interface run.
from strategy_poker import interactive_strategy, ai_strategy
from typing import Any, Callable
from game import Poker

# TODO: Replace None with the corresponding class name for your games.
# 's' should map to your implementation of Subtract Square, and 'c' should map
# to Chopsticks.

# The strategies you are to implement.  See strategy_poker.py, and then decide
# how to modify this.


class GameInterface:
    """
    A game interface for a Texas Hold'em Poker game.
    """

    def __init__(self, game: Poker, starting_amount: int, small_blind: int)\
            -> None:
        """
        Initialize this GameInterface, setting its active game to game,
        setting the starting starting_amount amount to starting_amount,
        the minimum bet amount to blind,
        the number of players to amount_of_players.
        """

        self.game = game
        self.game.starting_amount = starting_amount
        self.game.small_blind = small_blind
        self.p1_strategy = interactive_strategy(game)
        self.ai_strategy = ai_strategy(game)

    def play(self) -> None:
        """
        Play the game.
        """
        current_state = self.game.current_state
        print(current_state.current_leaderboards())

        # Pick moves until the game is over
        while not self.game.game_over(current_state):
            move_to_make = None

            # Print out all of the valid moves
            possible_moves = current_state.get_possible_moves()
            print("The current available moves are:")
            for move in possible_moves:
                print(move)

            # Pick a (legal) move.
            while not current_state.is_valid_move(move_to_make):
                current_strategy = self.p2_strategy
                if current_state.get_current_player_name() == 'p1':
                    current_strategy = self.p1_strategy
                move_to_make = current_strategy(self.game)

            # Apply the move
            current_player_name = current_state.get_current_player_name()
            new_game_state = current_state.make_move(move_to_make)
            self.game.current_state = new_game_state
            current_state = self.game.current_state

            print("{} made the move {}. The game's state is now:".format(
                current_player_name, move_to_make))
            print(current_state)

        # Print out the winner of the game
        if self.game.is_winner("p1"):
            print("Player 1 is the winner!")
        elif self.game.is_winner("p2"):
            print("Player 2 is the winner!")
        else:
            print("It's a tie!")


if __name__ == '__main__':
    starting_ammount = int(input('Enter the starting amount of money for each player: '))
    blind = int(input('Enter the small blind amount: '))

    GameInterface(Poker, starting_ammount, blind).play()
