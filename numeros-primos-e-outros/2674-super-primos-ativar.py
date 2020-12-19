def eh_primo(x):
    if (x==3) or (x==2):
        return True
    if (x<2) or (x%2==0):
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i==0:
            return False    
    return True

def sup_primo(num):
    while num >= 10:
        sup = num % 10
        num = int(num / 10)
        if not eh_primo(sup):
            return 0
    if((num == 2) or (num == 3) or (num == 5) or (num == 7)):
        return True
    else:
        return False

while(True):
    try:
        # (Entrada)
        n = input()
        if len(n)==0:
            break
        else:
            n = int(n)
        if not eh_primo(n):
            print("Nada")
        else:
            if sup_primo(n):
                print("Super")
            else:
                print("Primo")
    except EOFError:
        break

