# python 3

n = int(input())
 
moedas = list(map(int, input().split()))
moedas.sort(reverse=True)
 
total = 0
 
for moeda in moedas:
  total += moeda
 
maiorParte = 0
moedasNecessarias = 0
 
for moeda in moedas:
  maiorParte += moeda
  moedasNecessarias += 1
  if maiorParte > total/2:
    break
 
print(moedasNecessarias)
