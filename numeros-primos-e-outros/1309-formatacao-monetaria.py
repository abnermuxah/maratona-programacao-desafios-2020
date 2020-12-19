while True:
    try:
        dinheiro = '$'
        nota = input()
        if len(nota) == 0:
            break
        x = 1
        y = 3
        aux = ''
        for t, i in enumerate(reversed(nota)):
            aux += i
            if(((t+1)%y == 0) and (t!=int(len(nota))-1)):
                aux += ','
            x += 1
        dinheiro += aux[::-1]
        cent = input()
        if(len(cent) < 2):
            cent = '0'+cent
        #print("centavos",cent)
        print('{}.{}'.format(dinheiro, cent))
    except EOFError:
        break
    