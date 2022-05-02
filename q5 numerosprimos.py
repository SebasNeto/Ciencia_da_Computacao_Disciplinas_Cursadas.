entrada = 0
lista = []
def encontrar(entrada2):
    primo = True
    if entrada2 == 1 or entrada2 == 0 or entrada2 == -1:
        return False
    for c in range(entrada2):
            if c > 1 and entrada2 % c == 0:
                primo = False
    return primo
while(entrada != 99):
    entrada = int(input())
    if entrada != 99:
        lista.append(encontrar(entrada))
print(lista)
