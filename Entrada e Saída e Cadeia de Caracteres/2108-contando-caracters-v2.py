s = 0
while True:
    frase = input().split()
    sizes = []
    if frase == ['0']:
        break
    for i in frase:
        sizes.append(str(len(i)))
        if len(i) >= s:
            s = len(i)
            b = i
    p = '-'.join(sizes)
    print(p)

print()
print('The biggest word: %s' % b)