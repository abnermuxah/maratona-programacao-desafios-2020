T = True
while T == True:
    caso_teste = int(input())
    anterior = 0
    n = 0
    lista = []
    while not(n == caso_teste):
        lista.append(input())
        if not anterior:
            for i in range(len(conjunto) - 1):
                if (lista[-1] in lista[i]) or (lista[i] in lista[-1]):
                    anterior = 1
                    break
        n -= 1

    if anterior:
        print('Conjunto Ruim')
    else:
        print('Conjunto Bom')
    if caso_teste == 0:
        T = False