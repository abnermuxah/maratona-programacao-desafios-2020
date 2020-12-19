# 3 - Digame a Frequencia (1251)
chars = []
while True:    
    n = input()
    if (len(n)>0):
        chars.append(n)
    chars2 = {}
    for i in range(len(chars)):
        for j in range(len(chars[0])):
            if ord(chars[i][j]) not in chars2:
                chars2[ord(chars[i][j])]=0
            if ord(chars[i][j])  in chars2:
                chars2[ord(chars[i][j])]+=1
            valor = sorted(chars2.items(), reverse=True)
        del chars2
        chars2 = {}
        for x in range(len(valor)):
            print(valor[x][0],":",valor[x][1])
        print()
    if len(n)==0:
        break


