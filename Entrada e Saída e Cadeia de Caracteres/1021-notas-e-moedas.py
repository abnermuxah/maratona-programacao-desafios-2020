N =  float(input())
#N = 576.73
#N = 4
#N = 91.01
if (0 <= N <= 1000000.00):
    NOTAS = [100, 50, 20, 10, 5, 2]
    print("NOTAS:") #TEM QUE TA IGUAL A SAIDA DO PROBLEMA
    for i in range(len(NOTAS)):
        qtd_nota = int(N / NOTAS[i]) # valor informado divido pelo valor do indice atual é a qtd de nota em questão
        print(qtd_nota,"nota(s) de R$", "{:.2f}".format(NOTAS[i]) )
        # subtrarir a diferença das notas colocadas acima
        N -= qtd_nota * NOTAS[i]
    # o mesmo raciocinio aplica-se as muedas
    MOEDAS = [1, 0.5, 0.25, 0.10, 0.05, 0.01]
    print("MOEDAS:")
    #print("%.2f"%N)
    for i in range(len(MOEDAS)):
        qtd_nota = int(N / MOEDAS[i]) # valor informado divido pelo valor do indice atual é a qtd de nota em questão
        print(qtd_nota,'moeda(s) de R$', "{:.2f}".format(MOEDAS[i]))
        # subtrarir a diferença das notas colocadas acima
        N -= qtd_nota * MOEDAS[i]
        N = round(N,2)
        "{:.2f}".format(5)
else:
    print("dinheiro invalido, ta dando certo nao carai, tenta de novo ai")
