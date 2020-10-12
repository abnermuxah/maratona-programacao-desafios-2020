#1110-jogando-cartas-fora
T = True
while T == True:
  cartas = int(input())
  fim = []
  num = []
  if cartas == 0:
    T = False
    break
  for i in range(1, cartas+1):
    num.append(i)
  while (len(num) > 1):
    fim.append(str(num.pop(0)))
    num.insert(len(num) - 1, num.pop(0))
  print("Discarded cards: " + ", ".join(fim), "\nRemaining card: " + str(num[0]), end="\n")