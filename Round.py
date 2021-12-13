class Round:

    rounds = {}

    def __init__(
            self, id,
            nWolves, nSheep, nProtectedSheep, nVulnerableSheep, nAttackingWolves,
            taxRate, theftSuccessProbability, taxPool, nSuccessfulThefts, theftPool,
            wolfWoolPool, woolPerWolf
        ):
        self.id = id
        self.nWolves = nWolves
        self.nSheep = nSheep

        self.nProtectedSheep = nProtectedSheep
        self.nVulnerableSheep = nVulnerableSheep
        self.nAttackingWolves = nAttackingWolves

        self.taxRate = taxRate
        self.theftSuccessProbability = theftSuccessProbability
        self.taxPool = taxPool
        self.nSuccessfulThefts = nSuccessfulThefts
        self.theftPool = theftPool

        self.wolfWoolPool = wolfWoolPool
        self.woolPerWolf = woolPerWolf

        Round.rounds[id] = self

    def __str__(self):
        return str(vars(self))