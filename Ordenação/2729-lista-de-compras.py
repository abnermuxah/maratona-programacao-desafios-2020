# 5 - Lista de Compras (2729)
n = int(input())
i = 0
itens = []
while i != n:
    lista = input()
    lista1 = lista.split()
    lista1 = set(lista1)
    lista1 = sorted(lista1)
    itens.append(lista1)
    i+=1
for i in range(len(itens)):
    out = " ".join(itens[i])
    print(out)