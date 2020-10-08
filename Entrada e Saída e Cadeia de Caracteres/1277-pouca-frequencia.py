T = int(input())
saida = []
for n in range(T):
    qtd_estudantes = int(input())
    _nome = str(input()) # lista com os nomes dos alunos
    _freq = str(input()) # lista com a frequencia do respectivo aluno i
    nome = _nome.split(" ")
    freq = _freq.split(" ")
    aprovados = []
    for i in range(qtd_estudantes):
        total = len(freq[i])
        A = freq[i].count("A") # Ausente
        P = freq[i].count("P") # Presente
        M = freq[i].count("M") # Atestado
        total = total - M
        if (P/total < 0.75):
            aprovados.append(nome[i])
    if len(aprovados) == 0:
        saida.append(" ")
    else:
        saida.append(aprovados)
# se a lista de aprovados for vazia, coloca um valor vazio
# se a lista aprovados tiver negoço, dá um append
for i in range(len(saida)):
    for j in range(len(saida[i])):
        if len(saida[i])>1:
            print(saida[i][j], end=" ")
        else:
            print(saida[i][j])

