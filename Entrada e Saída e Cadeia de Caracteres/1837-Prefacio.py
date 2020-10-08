
# entrada (a e b) string
entrada = str(input())
e = entrada.split()
if (-1000 <= int(e[0]) < 1000):
    a = int(e[0])
else:
    print("inteiro invalido, tente de novo")

if (-1000 <= int(e[1]) < 1000 ):
    b = int(e[1])
else:
    print("inteiro invalido, tente de novo")
if a > 0  and b > 0: 
    q = int(a/b)
    r = int(a%b)
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = int((a - r)/b)
        break
print(q, end=" ")
print(r)
