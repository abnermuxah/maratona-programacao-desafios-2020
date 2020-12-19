def eh_primo(x):
    if (x==3) or (x==2):
        return True
    if (x<2) or (x%2==0):
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i==0:
            return False    
    return True
h, d, vel, count = 0,0,0,0
peso = int(input())
while(count < 10):
    if eh_primo(peso):
        count +=1
        vel = vel + peso
        peso+=1
    else:
        peso+=1
h = int((60000000/vel))
print(vel,'km/h')
d = int((h/24))
print(h,'h /',d,'d')