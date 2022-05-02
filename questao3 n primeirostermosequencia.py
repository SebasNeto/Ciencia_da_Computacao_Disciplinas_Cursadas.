N = int(input())
lista = []
contagem = 0
atual = 0
anterior = 0
razao = 1
while(contagem < N):
	atual = anterior + razao
	anterior= atual
	razao += 1
	contagem += 1
	lista.append(atual)
print(lista)
