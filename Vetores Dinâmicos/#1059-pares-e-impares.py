#1059-pares-e-impares
# entrada
N = int(input())
impar = [] 
par = [] 
for i in range(N):
    numero = int(input())
    if (False == (numero % 2 == 0)):
        impar.append(numero)
    elif (True):
        par.append(numero)
impar.sort(reverse=True)
par.sort(reverse=False)
for i in range(len(par)):
    print(par[i])
for i in range(len(impar)):
    print(impar[i])