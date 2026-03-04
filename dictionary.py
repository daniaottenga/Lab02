class Dictionary:

    def __init__(self, parola_aliena: str):
        self.parola = parola_aliena
        self.traduzioni = []

    def addWord(self, parola: str):
        self.parola_aliena = parola

    def translate(self):
        return self.traduzioni

    def translateWordWildCard(self):
        pass