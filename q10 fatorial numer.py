def funcao(n):
    if n < 0:
        return " N"
    elif n == 1 or n == 0:
        return 1
    else:
        fatorial = 1
        while(1 < n):
            fatorial *= n
            n -= 1
        return fatorial 

inici = 0
lista = []
while(inici < 10):
    entrada = int(input())
    lista.append(entrada)
    inici += 1
for c in range(len(lista)):
    print(funcao(lista[c]))
