# entrada (string o espaço vira -)
# analisa a primeira e a ultima palavra antes do - se for c armazena numa string
# faz a mesma coisa pros proximas palavras o,b,o,l 
# se formar cobol diz a palavra Grade
# se nao formar diz a palavra BUGA 


#frase = str(input())

#frase = "cap-one-best-opinion-language"

#frase = "Ana-number-once-a-night"
num = 0
while True:
    frase = str(input())
    x = frase.split("-")
    saida = []
    for i in range(len(x)):
        if (x[i][-1] == 'c' or x[i][0] == 'c'):
            saida.append("c")
           
        if (x[i][-1] == 'o' or x[i][0] == 'o'):
            saida.append("o")
            
        if (x[i][-1] == 'b' or x[i][0] == 'b'):
            saida.append("b")
           
        if (x[i][-1] == 'l' or x[i][0] == 'l'):
            saida.append("l")
    

    if saida.count("c") >= 1 and saida.count("o") >= 2 and saida.count("b") >= 1 and saida.count("l") >= 1: 
        print("GRACE HOPPER")
    else:
        print("BUG")