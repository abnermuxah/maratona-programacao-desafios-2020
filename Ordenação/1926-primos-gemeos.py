"""
1 ler os casos de teste Q (entrada)
2 laço de Q até i = 0 (para cada caso de teste)
3 armazenar em uma lista os total de primos gemeos no interval (X-Y) (processamento)
4 exibir a lista em um novo laço (saida)
"""

def eh_primo(x,y):
    primos = []
    for i in range(x,y+1):
        aux = 0
        for y in range(x,y+1):
            if i%y==0:
                aux +=1
        if aux <= 2:
            primos.append(i) 
    return primos
        

def eh_primo_gem(N):
    x = int(N[0])
    y = int(N[2])
    # pegar os primos do intervalo x e y
    z = eh_primo(x,y)
    return z


i = 0
out = []
Q = int(input())
while True:
    if Q == i:
        break
    N = input()
    total = eh_primo_gem(N)
    out.append(total)
    Q -= 1

print(total)
print(out)