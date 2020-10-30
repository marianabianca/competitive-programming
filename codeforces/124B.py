# python 3

from itertools import permutations

n, k = list(map(int, input().split(" ")))

permutacoes = []

for i in range(n):
  x = list(input())
  permuts = [''.join(x) for x in list(permutations(x))]
  permuts = list(map(int, permuts))
  permutacoes.append(permuts)

menor_dif = 10000000000

for i in range(len(permutacoes[0])):
  p = []
  for j in range(len(permutacoes)):
    aux = permutacoes[j][i]
    p.append(aux)
  dif = max(p) - min(p)
  if dif < menor_dif: menor_dif = dif

print(menor_dif)
