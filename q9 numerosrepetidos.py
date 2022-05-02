lista = []
listavazia = []
while True:
    n = int(input())
    lista.append(n)
    if n == -1:
        break
for i in range(len(lista)):
    for j in range(len(lista)):
        if i != j:
            if lista[i] == lista[j] and lista[i] not in listavazia:
                listavazia.append(lista[i])
                
print(listavazia)
    
