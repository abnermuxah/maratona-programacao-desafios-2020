# 2 - olimpiadas de natal (2018)
placar = {}
# placar = (pais : (x1, x2, x3)) 1 ouro 2 prata 3 bronze
while True:
    nome_prova = input()
    if len(nome_prova)==0:
        break
    for i in range(3):
        pais = input()
        if pais not in placar:
            placar[pais] = [0,0,0]
        if pais in placar:
            if i == 0:
                placar[pais][0] += 1
        if pais in placar:
            if i == 1:
                placar[pais][1] += 1
        if pais in placar:
            if i == 2:
                placar[pais][2] += 1
            # pais : (1, 2, 3)
print("Quadro de medalhas: ")
for pais in placar:
    print(pais,placar[pais][0],placar[pais][1],placar[pais][2])
