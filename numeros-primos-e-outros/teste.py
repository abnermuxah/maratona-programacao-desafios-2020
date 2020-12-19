while True:
    try:
        dinheiro = []
        nota = input()
        cent = input()
        if(len(cent) < 2):
            cent += '0'
            cent = cent[::-1]
        dinheiro += '.' + cent
        print(dinheiro)
    except EOFError:
        break