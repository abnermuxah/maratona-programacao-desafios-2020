tam = 12 # matriz é sempre quadrada
op = input()
matriz=[]
# ler os val1
# da matriz
for i in range(tam):
    lista = []
    for j in range(tam):
        valor = float(input())
        lista.append(valor)
    matriz.append(lista)
#imprimir a matriz
#print(matriz)
# se S entao somar todos elementoss acima da diagonal princial
if (op == 'S'):
    total = 0
    for i in range(tam):
        for j in range(tam):
            if not (i>j) and not (i==j):
                total += matriz[i][j]
    # exibir a soma total acima da diagonal principal
    print("{:.1f}".format(total))
# se M então calcular media acima da diagnonal principal
elif (op == 'M'):
    total = 0
    contador = 0
    for i in range(tam):
        for j in range(tam):
            if not (i>j) and not (i==j):
                total += matriz[i][j]
                contador = contador + 1
    total = total/(contador)
    print("{:.1f}".format(total))