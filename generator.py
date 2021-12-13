import Token
from Sheep import Sheep
from Wolf import Wolf
import random
import numpy as np

def randomBid():
    # get one number from beta distribution (0,1)
    # https://homepage.divms.uiowa.edu/~mbognar/applets/beta.html
    return round(np.random.beta(2.5, 10) * 100)

def randomAsk():
    # TODO: flip this
    return round(np.random.beta(2.5, 10) * 100)

def newTaxes(tokens):
    for token in tokens:
        if token.character == Token.Character.WOLF:
            token.ask = randomAsk()
        elif token.character == Token.Character.SHEEP:
            token.bid = randomBid()

def generateNWolves(N):
    wolves = []
    for _ in range(N):
        newAsk = randomAsk()
        wolf = Wolf(newAsk)
        wolves.append(wolf)
    return wolves

def generateNSheep(N):
    sheeps = []
    for _ in range(N):
        newBid = randomBid()
        sheep = Sheep(newBid)
        sheeps.append(sheep)
    return sheeps
