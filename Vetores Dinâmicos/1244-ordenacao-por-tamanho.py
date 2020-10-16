T = int(input())
i = int(0)
while (i != T):
    texto = str(input())
    texto_ord = sorted(texto.split(), reverse=True, key=len)
    print(" ".join(texto_ord))
    i = i + 1