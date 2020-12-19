# 3 Hiperprimos (1602)

"""
    1 RECEBER UM NUMERO
    2 CONTAR QUANTOS DIVISORES ESSE NUMERO POSSUI E ARMAZENAR NUMA LISTA
    3 VERIFICAR SE ESSE NUMERO E PRIMO 
"""
lista1 = []
while True:
    num = input()
    if len(num)==0:
        break
    lista1.append(num)

print(primos1)
