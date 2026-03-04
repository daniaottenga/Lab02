import translator as tr

t = tr.Translator()

txtIn = ""
while txtIn != 5:

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("OK, quale parola devo aggiungere?")

        indicatore = False
        while indicatore == False:
            txtIn = input().lower().split()
            indicatore = True
            for parola in txtIn:
                if not parola.isalpha():
                    indicatore = False

        parola = txtIn[0]
        traduzioni = " ".join(txtIn[1:])
        tupla = (parola, traduzioni)
        t.handleAdd(tupla)

        print("['", tupla[0], "'", end = "")
        l = tupla[1].split()
        for elemento in l:
            print(", '", elemento, "'", end = "")
        print("]")


    elif int(txtIn) == 2:
        print("OK, quale parola devo cercare?")
        indicatore = False
        while indicatore == False:
            txtIn = input().lower()
            if txtIn.isalpha():
                indicatore = True

        traduzione = t.handleTranslate(txtIn)
        if traduzione == None:
            print("NO")
            continue

        if len(traduzione.split()) > 1:
            l_traduzione = traduzione.split()
            print("[", end = "")
            for i in range(len(l_traduzione)):
                if i == 0:
                    print("'", l_traduzione[i], "'", end = "")
                else:
                    print(", '", l_traduzione[i], "'", end = "")
            print("]")
        else:
            print(f"['{traduzione}']")


    elif int(txtIn) == 3:
        print("OK, quale parola devo cercare?")
        indicatore = False
        while indicatore == False:
            indicatore = True
            txtIn = input().lower()
            for char in txtIn:
                if char != "?" and not char.isalpha():
                    indicatore = False
            if txtIn.count("?") != 1:
                indicatore = False

        traduzione = t.handleWildCard(txtIn)
        if traduzione == "":
            print("NO")
            continue

        if len(traduzione.split()) > 1:
            traduzione.split()
            print("[", end="")
            for i in range(len(traduzione)):
                if i == 0:
                    print("'", traduzione[i], "'", end="")
                else:
                    print(", '", traduzione[i], "'", end="")
            print("]")
        else:
            print(f"['{traduzione}']")


    elif int(txtIn) == 4:
        t.stampa()

    elif int(txtIn) == 5:
        break