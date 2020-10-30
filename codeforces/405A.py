# python 2.7
# coding: utf-8

n = int(raw_input())
ent = map(int, raw_input().split())
ent.sort()

resposta = ""
for i in ent:
    resposta += str(i) + " "

resposta.strip()
print resposta
