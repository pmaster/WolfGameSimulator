from Token import Token, Character


class Wolf(Token):
    def __init__(self, ask = 20, alpha = 5):
        Token.__init__(self, Character.WOLF)
        self.ask = ask
        self.alpha = alpha

        # boolean
        self.roundAttacked = {}

    def getTax(self):
        return self.ask

    def setTax(self, tax):
        self.ask = tax