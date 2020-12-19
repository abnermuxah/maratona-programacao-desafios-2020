#1874-empurrando-blocos
# para cada caso de teste:
# H : Altura da pilha mais a direita (linhas)
# P : Qtd de pilha de blocos (colunas valores)
# F : Tamanho da fila
# inicio do laço (while)
# ---- Entradas ----- #
ent = str(input())
ent = ent.split()
H = int(ent[0])
P = int(ent[1])
F = int(ent[2])
blocos = []
# se HPF === 0 (break)
# ---- Processamento ---- #
for i in range(H): # leitura da pilha em linha cada linha é uma camda 
    val = str(input())
    val = val.split()
    if (len(val)<=P): 
        blocos.append(val)
    else:
        break
# leitura da lista 
lista = str(input())
lista = lista.split()


# --- Processamento ---


for i in range(F-1,-1,-1):
    for j in range(-1,F-1,1):
        if int(blocos[i][j]) == 0 and len(lista)>0:
            aux = lista.pop()
            blocos[i].pop(j)
            blocos[i].insert(j, aux)

for i in range(F):
    print(blocos[i])


