import Token
import generator
from Sheep import Sheep
from Wolf import Wolf
import Game
from Round import Round

import numpy as np
import statistics
from statistics import median
import random

def printResults(tokens):
    print(f'Results of {Game.round_id}')
    print(f'Round info:')
    print(Round.rounds[Game.round_id])
    print(f'Format: token, tax signal, delta, current wool')
    for token in tokens:
        if token.character == Token.Character.WOLF:
            print(
                f'{token.character.name} {token.id}: ' +
                f'tax {token.getTax()}; ' +
                f'+{token.roundDeltas[Game.round_id]} wool, ' +
                f'now: {token.wool}'
            )
    for token in tokens:
        if token.character == Token.Character.SHEEP:
            print(
                f'{token.character.name} {token.id}: ' +
                f'tax {token.getTax()}; ' +
                f'+{token.roundDeltas[Game.round_id]} wool, ' +
                f'now: {token.wool}'
            )


wolves = generator.generateNWolves(3)
sheeps = generator.generateNSheep(27)
stakedTokens = wolves + sheeps

for _ in range(5):
    Game.computeRound(stakedTokens)
    printResults(stakedTokens)
    generator.newTaxes(stakedTokens)