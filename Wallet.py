# wallets hold tokens
class Wallet:

    current_address = 100

    def __init__(self):
        self.tokens = []
        Wallet.current_address += 1
        self.address = Wallet.current_address

    def numTokens(self):
        return len(self.tokens)

    def addToken(self, token):
        self.tokens.append(token)