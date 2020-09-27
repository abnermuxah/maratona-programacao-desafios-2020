T = int(input())

#T = 1
# entrada (jogada1 (espaço) jogada 2) para cada rodada
jogadas = []
for i in range(T):
    jogadas.append(input())
# processamento e saida (para cada condição) agrupo a lista e avalio cada item
if (1 <= T <= 100):
    for i in range(T):
        analise = str(jogadas[i]).split() # dividir a string em 2 e depois analizar
        print(analise)
        if (analise[0] == analise[1]):
            print('Caso #'+ str(i) + ': De Novo!')
        else:
            print('Caso #'+ str(i) + ': Raj trapaceou!')
        if (analise[0] == 'tesoura' and analise[1] == 'papel'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'papel' and analise[1] == 'pedra'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'pedra' and analise[1] == 'lagarto'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'lagarto' and analise[1] == 'Spock'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'Spock' and analise[1] == 'tesoura'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'tesoura' and analise[1] == 'lagarto'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'lagarto' and analise[1] == 'papel'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'papel' and analise[1] == 'Spock'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'Spock' and analise[1] == 'pedra'):
            print('Caso #'+ str(i) + ': Bazinga!')
        if (analise[0] == 'pedra' and analise[1] == 'tesoura'):
            print('Caso #'+ str(i) + ': Bazinga!')
        




