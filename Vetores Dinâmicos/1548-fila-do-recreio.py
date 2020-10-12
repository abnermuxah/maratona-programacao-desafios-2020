#1548 Fila do recreio´
T = int(input())
while (T > 0):
    alunos = int(input())
    notas = input().split()
    for id, i in enumerate(notas):
        notas[id] = int(notas[id])
    tot = 0
    notas_ord = sorted(notas) # ordenar as notas
    notas_ord.reverse()
    for id, i in enumerate(notas):
        if (notas[id] == notas_ord[id]):
            tot = tot + 1
    print(tot)
    T = (T - 1)