num_linhas = int(input())
for i in range (num_linhas):
    texto = input()
    # dividir a linha por 2 (texto1 e texto 2)
    div = int(len(texto)/2)
    # salvar a primeira parte em texto 1
    texto1 = texto[:div]
    # inverter a string 
    texto1 = texto1[::-1]

    # salvar a segunda parte em texto 2
    texto2 = texto[div:]
    # inverter a string 
    texto2 = texto2[::-1]

    # juntar as duas strings
    print(texto1 + texto2)

    #pronto ta funcionando caraca! 

