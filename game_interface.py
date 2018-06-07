# TODO: import the modules needed to make game_interface run.
from strategy_poker import *
from typing import Any, Callable
from game import Poker


# TODO: Replace None with the corresponding class name for your games.
# 's' should map to your implementation of Subtract Square, and 'c' should map
# to Chopsticks.
# playable_games = {'s': SubtractSquareGame,
#                   'c': Chopsticks}

# The strategies you are to implement.  See strategy_poker.py, and then decide
# how to modify this.
# usable_strategies = {'r': random_strategy,
#                      'i': interactive_strategy}


class GameInterface:
    """
    A game interface for a game of poker, up to nine players.
    """
    game: Any
    player_strategy: Callable[[Any], Any]
    ai_strategy: Callable[[Any], Any]

    def __init__(self, game: "Poker", player_strategy: Callable, ai_strategy: Callable[[Any], Any],
                 lucky_number: int) -> None:
        """
        Initialize this GameInterface, setting its active game to game.
        """
        self.game, self.player_strategy, self.ai_strategy, self.lucky_number = game, player_strategy,\
                                                                               ai_strategy, lucky_number

    def play(self) -> None:
        """
        Play the game.
        """
        # Create new rounds until the game is over
        while not self.game.game_over():
            current_round = self.game.round
            # Create new rotations until the round is over:
            while not current_round.round_over():
                for stage in range(4):

                    current_rotation = current_round.current_rotation
                    # pick moves until rotation is over
                    while not current_rotation.rotation_over():
                        move_to_make = None

                        # Print out all available moves:
                        possible_moves = current_rotation.get_possible_moves()
                        print("The current available moves are:")
                        for move in possible_moves:
                            print(move)
                            if move == "Call":
                                print("To call - {}".format(current_rotation.get_current_player().to_call))

                        # Pick a (legal) move:
                        while not current_rotation.is_valid_move(move_to_make):
                            current_strategy = self.ai_strategy
                            if current_rotation.get_current_player().name == ("Player" + str(self.lucky_number)):
                                current_strategy = self.player_strategy
                            move_to_make = current_strategy()

                        # Apply the move:
                        current_player_name = current_rotation.get_current_player()
                        new_rotation = current_rotation.make_move(move_to_make)
                        self.game.round.current_rotation = new_rotation
                        current_rotation = self.game.round.current_rotation
                        print("{} made the move {}.".format(current_player_name, move_to_make))

                    # After each stage print out the new community cards:
                    if stage == 1:
                        current_round.community_cards_open = current_round.community_cards_hidden[0:3]
                        print("The flop is: {}, {}, {}.".format(current_round.community_cards_hidden[0],
                                                               current_round.community_cards_hidden[1],
                                                               current_round.community_cards_hidden[2]))
                    elif stage == 2:
                        current_round.community_cards_open = current_round.community_cards_hidden[0:4]
                        print("The turn is: {}.".format(current_round.community_cards_hidden[3]))
                    elif stage == 3:
                        current_round.community_cards_open = current_round.community_cards_hidden[0:5]
                        print("The turn is: {}.".format(current_round.community_cards_hidden[4]))

                    # Print out the known community cards every new rotation:
                    community_cards = ''
                    for card in range(len(current_round.community_cards_open) - 1):
                        community_cards += "{}, ".format(current_round.community_cards_open[card])
                    community_cards += "{}.".format(current_round.community_cards_open[-1])
                    print("The community cards are: {}".format(community_cards))


            # Print out the hand winner:
            print("The winner of this hand is: {} with {}{}, getting ${}".format(current_round.hand_winner().name,
                                                                                 current_round.hand_winner().hand[0],
                                                                                 current_round.hand_winner().hand[1],
                                                                                 current_round.current_pot))
        # Print out the game winner and the leaderboards:
        print("The champion is {} with total earnings of ${}".format(self.game.game_winner().name,
                                                                     self.game.game_winner().bank))
        print("The leaderboard:")
        print(self.game.current_leaderboards())


if __name__ == '__main__':
    number_of_players = 0
    while number_of_players not in range(1, 9):
        # Ask the amount of players, turn into int
        number_of_players = int(input("What is the number of players in the game? Max: 9"))
    # Ask the starting bank for each player, turn into int
    starting_bank = int(input("What is the starting bank for each player?"))
    # Ask the small blind amount, turn into int
    small_blind = int(input("What is the small blind?"))
    lucky_number = int(input("Favorite number 1-{}?".format(number_of_players)))

    GameInterface(Poker(starting_bank, small_blind, number_of_players), interactive_strategy(), ai_strategy(),
                  lucky_number).play()
