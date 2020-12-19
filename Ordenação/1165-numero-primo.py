# 1 - Numero Primo (1165)
def eh_primo(num):
    for i in range(len(num)):
        aux = 0
        for j in range(1,num[i]):
            if num[i]%j==0:
                aux +=1
        if aux <= 2:
            print(num[i],'Prime')
                
        else:
            print(num[i],'Not Prime')
            

if __name__ == "__main__": 
    n = int(input())
    out = []
    primos = []
    for i in range(n):
        num = int(input())
        primos.append(num)
    eh_primo(primos)
    
    # algoritmo de 0 a N
"""
def eh_primo(num):
    for x in range(1,num+1):
        aux = 0
        for y in range(1,num+1):
            if x%y==0:
                aux +=1
        if aux <= 2:
            print(x, "eh primo")
        else:
            print(x,"nao eh primo")
"""
# algoritmo de que so imprime N