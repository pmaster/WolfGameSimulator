from Token import Token, Character

class Sheep(Token):
    def __init__(self, bid = 20):
        Token.__init__(self, Character.SHEEP)
        self.bid = bid

        # boolean
        self.roundVulnerable = {}
        # boolean
        self.roundStolenFrom = {}
        # numbers
        self.roundTaxPaid = {}

    def getTax(self):
        return self.bid

    def setTax(self, tax):
        self.bid = tax