n = -1
lista = []
entrada = 0
entrada2 = 0
cont1 = 0
cont2 = 0
while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)
    
for c in range(len(lista)):
    if lista[c] % 2 == 0:
        entrada += lista[c]
        cont1 +=1
    else:
        entrada2 += lista[c]
        cont2 += 1
if cont1 == 0 and cont2 == 0:
    media = 0.0
    media2 = 0.0
elif cont2 == 0:
    media2 = 0.0
    media = entrada/cont1
elif cont2 == 0:
    media2 = entrada2/cont2
    media = 0.0
else:
    media = entrada/cont1
    media2 = entrada2/cont2
print(round(media,2))
print(round(media2,2))

