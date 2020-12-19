lista = []
while True:
    try:
        nome = input()
        lista.append(nome))  
    except EOFError:
        break
lista = sorted(lista, key=lambda x: x.lower())
ultimo = lista[len(lista)-1]
print(ultimo)