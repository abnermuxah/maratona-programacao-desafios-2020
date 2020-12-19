#1260-especies-de-arvores
T = int(input())
arvores=[]
print("\n", end="")
while (T!=0):
    qtd_max = 1000000
    max_especies = 10000
    i = 1
    while (i <= qtd_max): # ler a especie de arvore e ocorrencia com limite de entrada
        arvores.append(input())
        i = i + 1
    # transformar a lista em um conjunto ordenado de especies de arvores
    arvores.sort(reverse=True)
    especies = set(arvores)
    # para algoritmo se ultrapssar a qtd definida de especies
    if len(especies) > max_especies:
        break
    # analisar especie 1 a n contar na lista de arvores e printar na tela a qtde
    especies = list(especies)
    for i in range(len(especies)):
        print(especies[i], '%.4f' % arvores.count(especies[i]))
    print("\n", end="") # quebra de linha após encerrar o caso de teste 
    T = T-1