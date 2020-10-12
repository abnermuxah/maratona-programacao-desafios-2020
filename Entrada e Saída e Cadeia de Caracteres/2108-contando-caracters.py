v = 1
s = 0
while (v==1):
    tamanho = []
    frase = input().split()
    if frase == ['0']:
        v = 0
        break
    for i in frase:
        tamanho.append(str(len(i)))
        if len(i) >= s:
            b = i
            s = len(i)
    tam = '-'.join(tamanho)
    print(tam)

print("\nThe biggest word:", b)