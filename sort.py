import random

L = []
R = ["Dezembro","Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho"]
S = []
while True:
	n = str(input("Digite o nome da pessoa(Digite Sair para fechar):"))
	if n == "sair":
		break
	L.append(n)
	S.append(random.shuffle(R))
x = 0
while x < len(L):
	print(L[x], R[x])
	x=x+1



