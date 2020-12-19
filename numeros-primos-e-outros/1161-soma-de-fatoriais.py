from functools import reduce
def fatorial(n):
  if n < 1:
    return None if n < 0 else 1
  return reduce(lambda x, y: x * y, range(1, n + 1))

while True:
  try:
    num1,num2 = map(int,input().split())
    print(fatorial(num1)+fatorial(num2))
  except:
    break