from statistics import median
import Token
import random
from Round import Round
from math import floor, ceil

# contains all the game mechanics

# the upcoming round id
round_id = 0

dailyWoolGeneration = 1000
# non-tax paying sheep are at risk for being attacked, and the fear hampers their wool generation
scared_sheep_wool_generation_penalty_modifier = .5

# dict of dicts
# roundNumber : {medianTaxAsk, numAttackers, numDefenders}
rounds = {}

def computeRound(stakedTokens):
    global round_id
    round_id += 1

    wolves = [token for token in stakedTokens if token.character == Token.Character.WOLF]
    wolves.sort(key=lambda wolf: wolf.ask)
    nWolves = len(wolves)

    sheeps = [token for token in stakedTokens if token.character == Token.Character.SHEEP]
    sheeps.sort(key=lambda sheep: sheep.bid)
    nSheep = len(sheeps)

    round = {}

    # compute tax rate
    medianTaxAsk = median(wolf.getTax() for wolf in wolves)
    taxRate = medianTaxAsk

    # segment sheep based on vulnerability
    taxPaidSheeps = []
    vulnerableSheeps = []
    for sheep in sheeps:
        if sheep.bid >= medianTaxAsk:
            taxPaidSheeps.append(sheep)
        else:
            vulnerableSheeps.append(sheep)


    # compute attacking wolves
    nAttackingWolves = nWolves

    # compute vulnerable sheep
    nVulnerableSheeps = len(vulnerableSheeps)

    # compute probability of a successful attack
    # P(successful theft) = B * A_to_G * (V_to_C * N_attacking_chads / N_unprotected_virgins) ^ C_nl
    # The B coefficient relates to the base case and gives the probability of a successful
    # theft when all Chads attack and no Virgins have paid tax.
    #
    # V_to_C: the expected ratio of virgins to chads, based on mint probabilities.
    #
    # C_nl: coefficient of non-linearity, which facilitates outsized raid results,
    # where increasing the ratio of Chad Doges to Virgin Doges has an outsized impact,
    # enabling one side to overwhelm the other, like increasing the amount of footsoldiers
    # for one side on a battlefield, and vice versa.
    B = 0.2
    V_to_C = 9
    C_nl = 1.5
    theftSuccessProbability = B * ((V_to_C * nAttackingWolves / nVulnerableSheeps) ** C_nl)
    # bound theftSuccessProbability in [0,1]
    theftSuccessProbability = max(0, min(1, theftSuccessProbability))

    # compute each protected sheep's wool gain
    taxPool = 0
    nTaxPaidSheep = len(taxPaidSheeps)
    for sheep in taxPaidSheeps:
        woolGained = dailyWoolGeneration
        taxPaid = woolGained * taxRate / 100
        woolGained -= taxPaid
        taxPool += taxPaid

        sheep.wool += woolGained
        sheep.roundWoolCounts[round_id] = sheep.wool
        sheep.lastParticipatingRound = round_id
        sheep.roundDeltas[round_id] = woolGained
        sheep.roundVulnerable[round_id] = False
        sheep.roundStolenFrom[round_id] = False
        sheep.roundTaxPaid[round_id] = taxPaid


    # compute whether each vulnerable sheep got stolen from or not, and their wool gained
    nSuccessfulThefts = 0
    theftPool = 0
    nVulnerableSheep = len(vulnerableSheeps)
    for sheep in vulnerableSheeps:
        woolGained = dailyWoolGeneration * scared_sheep_wool_generation_penalty_modifier
        stealSuccessful = False
        if random.random() < theftSuccessProbability:
            nSuccessfulThefts += 1
            theftPool += woolGained # sheep.wool + woolGained, or just woolGained?
            woolGained = 0
            stealSuccessful = True

        sheep.wool += woolGained
        sheep.roundWoolCounts[round_id] = sheep.wool
        sheep.lastParticipatingRound = round_id
        sheep.roundDeltas[round_id] = woolGained
        sheep.roundVulnerable[round_id] = True
        sheep.roundStolenFrom[round_id] = stealSuccessful
        sheep.roundTaxPaid[round_id] = 0


    # compute each wolf's wool gain
    wolfWoolPool = taxPool + theftPool
    woolPerWolf = wolfWoolPool / nAttackingWolves
    for wolf in wolves:
        wolf.roundDeltas[round_id] = woolPerWolf
        wolf.roundAttacked[round_id] = True
        wolf.lastParticipatingRound = round_id
        wolf.wool += woolPerWolf

    Round(
        round_id,
        nWolves, nSheep, nTaxPaidSheep, nVulnerableSheep, nAttackingWolves,
        taxRate, theftSuccessProbability, taxPool, nSuccessfulThefts, theftPool,
        wolfWoolPool, woolPerWolf
    )