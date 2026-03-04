import translator as tr

t = tr.Translator()

txtIn = ""
while txtIn != 5:

    t.printMenu()

    lista = t.loadDictionary("dictionary.txt")

    while txtIn != int:
        txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("OK, quale parola devo aggiungere?")
        while txtIn != str:
            txtIn = input().lower().split()

        parole = []
        for i in range(len(txtIn)):
            if i == 1:
                pass
            else:
                parole.append(txtIn[i - 1])

        tupla = (txtIn[0], parole)
        t.handleAdd(tupla)

    if int(txtIn) == 2:
        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        pass
    if int(txtIn) == 5:
        break