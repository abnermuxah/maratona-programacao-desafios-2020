# 5 - Camisetas
n = int(input())
pedidos = {}
for i in range(n):
    nome = input()
    if nome == "0":
        break
    camisa = input()
    x, y = camisa.split(" ")
    pedidos[nome] = (x,y)
    x = sorted(pedidos.items(), reverse=True, key=lambda i : i[0])
    dict(x)
    y = sorted(x, key=lambda i : i[1])
    dict(y)
    for i in y:
        print(i[0],"\n",i[1][0], i[1][1])

"""
#n = 3
#pedidos = {'Maria Joao': ('branco','P'),'Marcio Gues': ('vermelho','P'),'Maria Jose': ('branco ','P')}
x = sorted(pedidos.items(), reverse=True, key=lambda i : i[0])
dict(x)
y = sorted(x, key=lambda i : i[1])
dict(y)
for i in y:
    print(i[0],"\n",i[1][0], i[1][1])
"""