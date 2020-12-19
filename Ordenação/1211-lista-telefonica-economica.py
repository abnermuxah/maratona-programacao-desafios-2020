# Questão 2 - Lista Telefônica Econômica 
n = int(input())
lista_tel = []
#n = 3
#lista_tel = [[5,3,5,4,5,6],[5,3,5,4,8,8],[8,3,5,4,5,6]]
#n = 2
#lista_tel = [[1,2,3,4,5],[1,2,3,5,4]]
max = 0
# leitura da lista
for i in range(n):
    num = list(input())
    lista_tel.append(num)
# procurar a linha com maior numero economizado
for i in range(n):
    for j in range(len(lista_tel[0])):
        if ((n-1) <= i):
            break
        if (lista_tel[i][j] == lista_tel[i+1][j]):
            max = max + 1
            if (j+1 < max):
                max = max -1
print(max)