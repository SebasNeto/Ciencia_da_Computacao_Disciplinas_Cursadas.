N = int(input())
lista = []
for c in range(N):
    N = int(input())
    if c == 0:
        lista.append(N)
    elif N > lista[-1]:
        lista.append(N)
    else:
        posicao = 0
        while posicao < len(lista):
            if N <= lista[posicao]:
                lista.insert(posicao, N)
                break
            posicao += 1
print(lista)
        
