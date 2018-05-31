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
        self.current_bet = 0
        self.to_call = 0
        self.is_turn = False
        self.name = name

    def __eq__(self, other) -> bool:
        equal = False
        if self.bank == other.bank:
            equal = True
        return equal
