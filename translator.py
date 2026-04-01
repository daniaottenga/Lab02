import dictionary as d

class Translator:

    def __init__(self, dizionario = d.Dictionary):
        self.dizionario = dizionario

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("-------------------------------\n\tTranslator Alien-Italian\n-------------------------------")
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario"
              "\n5. Exit\n-------------------------------\n")

    def loadDictionary(self, dict: str):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r') as file:
            for line in file:
                divisione = line.split()
                parola = divisione[0]
                traduzioni = divisione[1]
                tupla = (parola, traduzioni)
                self.dizionario.addWord(tupla)

    def handleAdd(self, entry: tuple):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dizionario.addWord(entry)

    def handleTranslate(self, query: str):
        # query is a string <parola_aliena>
        return self.dizionario.translate(query)

    def handleWildCard(self, query: str):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query)

    def stampa(self):
        self.dizionario.stampati()