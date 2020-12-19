out = []
while(True):
    try:
        # frase linha n criptografada (leitura)
        texto = ''
        frase = input()
        if len(frase)==0:
            break
        # tratamento da frase
        for i in range(len(frase)):
            if frase[i]=='@':
                texto +='a'
            if frase[i]=='&':
                texto +='e'
            if frase[i]=='!':
                texto +='i'  
            if frase[i]=='*':
                texto +='o'    
            if frase[i]=='#':
                texto +='u'
            elif frase[i] not in ('@','&', '!', '*', '#'):
                texto += frase[i]
        # adicionar frase descriptografada a lista texto
        out.append(texto)
    except EOFError:
        break

# saida (texto descriptografado)
#print(out)
for i in range(len(out)):
    print(out[i])
    