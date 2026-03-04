import dictionary as d

class Translator:

    def __init__(self):
        self.lista = []

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
                tupla = line.split()
                self.lista.append(d.Dictionary(tupla[0], tupla[1]))
        return self.lista


    def handleAdd(self, entry: tuple):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        oggetto = d.Dictionary(entry[0])
        self.lista.append(oggetto)


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass