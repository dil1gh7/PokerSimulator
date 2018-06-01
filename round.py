from current_state_poker import CurrentState
from random import shuffle

card_deck = ['2h', '2c', '2s', '2d', '3h', '3c', '3s', '3d', '4h', '4c',
             '4s', '4d', '5h', '5c', '5s', '5d', '6h', '6c', '6s', '6d',
             '7h', '7c', '7s', '7d', '8h', '8c', '8s', '8d', '9h', '9c',
             '9s', '9d', '10h', '10c', '10s', '10d', 'Jh', 'Jc', 'Js',
             'Jd', 'Qh', 'Qc', 'Qs', 'Qd', 'Kh', 'Kc', 'Ks', 'Kd',
             'Ah', 'Ac', 'As', 'Ad']


class Round:
    """
    A class for rounds
    """

    def __init__(self, small_blind: int, player_list: list) -> None:
        self.card_deck, self.current_pot, self.small_blind, self.player_list, self.big_blind =\
            card_deck, 0, small_blind, player_list, small_blind * 2
        self.community_cards = []
        for player in self.player_list:
            # Sets a player with position 0 to move in the beginning of each round
            if player.position == 0:
                player.is_turn = True
        # creates a state
        self.current_state = CurrentState(small_blind, player_list)

    def get_current_pot(self) -> int:
        """
        Returns a string with the current pot
        """
        return self.current_pot

    def hand_winner(self) -> None:
        """
        Determines the winner of the hand and adds the pot to the player's bank
        if the player is the winner
        """
        pass

    def round_over(self) -> bool:
        """
        Returns whether or not the hand is over
        """
        round_over = False
        if len(self.current_state.get_possible_moves()) == 0:
            round_over = True
        return round_over

    def hand_counter_inc(self) -> object:
        """
        Returns an incremented data of hand counter
        """
        pass

    def give_cards(self) -> None:
        """
        Shuffles and gives out the cards to the players and places the community cards, collects the blinds.
        """
        # Collect the blinds
        for player in self.player_list:
            if player.position == 1:
                player.bank -= self.small_blind
                self.current_state.current_pot += self.small_blind
            elif player.position == 2:
                player.bank -= self.big_blind
                self.current_state.current_pot += self.big_blind
        # Shuffle the deck
        shuffle(self.card_deck)
        # Give players their cards
        for player in self.player_list:
            player.hand.append(self.card_deck.pop())
            player.hand.append(self.card_deck.pop())
        # Place community cards
        for i in range(5):
            self.community_cards.append(self.card_deck.pop())



    def give_button(self):
        """
        Assigns dealer button to a random player
        player with position == 0 is the dealer, position == 1 is SB,
        position == 2 is BB


        """
        pass
