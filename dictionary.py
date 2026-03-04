class Dictionary:

    def __init__(self):
        self.dizionario = {}

    def addWord(self, tupla: tuple):
        self.dizionario[tupla[0]] = tupla[1]

    def translate(self, parola: str):
        return self.dizionario.get(parola)

    def translateWordWildCard(self, parola: str):
        traduzione = ""
        corretto = True
        for chiave in self.dizionario:
            l_chiave = list(chiave)
            i = 0
            i_max = len(l_chiave)
            for char in parola:
                if (i == i_max):
                    break
                if char == "?":
                    pass
                elif char != l_chiave[i]:
                    corretto = False
                i += 1
            if corretto == True:
                traduzione = self.dizionario[chiave]
                break
        return traduzione

    def stampati(self):
        for chiave in self.dizionario:
            print("['", chiave, "'", end = "")
            trad = self.dizionario[chiave]
            if len(trad.split()) > 1:
                trad.split()
                print("[", end="")
                for i in range(len(trad)):
                    print(", '", trad[i], "'", end="")
                print("]")
            else:
                print(f", '{trad}']")