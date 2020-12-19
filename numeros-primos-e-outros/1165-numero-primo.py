def eh_primo(x):
    if (x==3) or (x==2):
        return True
    if (x<2) or (x%2==0):
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i==0:
            return False    
    return True

n = int(input())
for i in range(0,n):
    num = int(input())
    out = eh_primo(num)
    if out == True:
        print(num, 'eh primo')
    else:
        print(num, 'nao eh primo')