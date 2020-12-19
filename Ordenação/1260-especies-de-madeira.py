n = int(input())
i = 0
while i != n:
    catalogo = {}
    total_arvores = 0
    # lendo e contando os dados em um dicionario
    while len(catalogo) <= 10000 and total_arvores < 1000000:
        especie = input()
        if len(especie)==0:
            break
        if especie not in catalogo:
            catalogo[especie]=0
        if especie in catalogo:
            catalogo[especie]+=1
    for especie in catalogo:
        print(especie,":",catalogo[especie])
    i+=1
