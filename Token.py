import Game
from enum import Enum

class Character(Enum):
    WOLF = 0
    SHEEP = 1

class Token:

    current_id = 1000

    def __init__(self, character):
        Token.current_id += 1

        self.id = Token.current_id
        self.character = character

        self.wool = 0
        self.lastParticipatingRound = None

        # history of wool counts in participating rounds
        self.roundWoolCounts = {}
        # history of PnL in participating rounds
        self.roundDeltas = {}
