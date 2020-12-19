# 5 - Troca de cartas (1104)
max_cartas = []
while True:
    n = input()
    if n == '0 0':
        break
    n = n.split(" ")
    max_A = n[0]
    max_B = n[1]
    A = input()
    B = input()
    # transformar A e B em um dicionario
    A = A.split(" ")
    B = B.split(" ")
    dic_A = {}
    dic_B = {}
    # transformar A em um dicionario (chave:valor)
    for i in range(len(A)):
        if A[i] not in dic_A:
            dic_A[A[i]] = 0
        if A[i] in dic_A:
            dic_A[A[i]] += 1
    # transformar B em um dicionario (chave:valor)
    for i in range(len(B)):
        if B[i] not in dic_B:
            dic_B[B[i]] = 0
        if B[i] in dic_B:
            dic_B[B[i]] += 1    
    # contar quantas chave:valor >= 2 (essas serão as cartas trocadas de A e B)
    total = 0
    for i in dic_A:
        if  dic_A[i]>=2:
            total +=1
    for i in dic_B:
        if  dic_B[i]>=2:
            total +=1
    max_cartas.append(total)

# saida (lista max_cartas por ordem de entrada)

for i in range(len(max_cartas)):
    print(max_cartas[i])