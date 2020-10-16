#1110-jogando-cartas-fora
# n cartas (1 até n)
# cartas 

while True:
    # ---- Entrada ------ #
    n = int(input())
    pilha = []
    descartadas = []
    if (n == 0):
        break
    # ---- Processamento ------ #
    for i in range(1,n+1):
        pilha.append(str(i))
    # enquanto pilha tiver um elemento (ultimo faça o seguinte)
    while (len(pilha)!=1):
        # salve e remova o item do topo da pilha em uma nova lista
        aux = pilha.pop(0)
        descartadas.append(str(aux))
        # coloque o elemento de baixo do topo na base da pilha
        aux = pilha.pop(0)
        pilha.append(aux)
    # ---- Saída ------ #
    # itens restantes
    print("Discarded cards:",", ".join(descartadas))
    # a ultima carta e o unico elemento da pilha
    print("Remaining card:", ", ".join(pilha))