T = int(input())
while T > 0:
    _frase = input()
    frase = _frase.split()
    frase.sort(reverse=True, key=len)
    for i in range(len(frase)):
        print(frase[i], end="")
        if i != (len(frase)-1):
            print(" ", end="")
    T = (T - 1)