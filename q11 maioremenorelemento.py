t = int(input())
N = [int(input())for i in range(t)]
maior = N[0]
i = 0
while i < len(N):
    if N[i] > maior:
        maior = N[i]
    i += 1
menor = N[0]
i = 0
while i < len(N):
    if N[i] < menor:
        menor = N[i]
    i += 1

print(menor,maior)

