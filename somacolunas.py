linha2 = []
matriz = []
somacoluna = []
for linha in range(4):
    for coluna in range(4):
        linha2.append(int(input()))
    matriz.append(linha2)
    linha2 = []

contc = 0
coluna2 = []
soma = 0
for c in range (0,len(matriz)):
    coluna2 = []
    for i in range(0,len(matriz)):
        coluna2.append(matriz[i][c])
    for x in range(len(coluna2)):
        soma += coluna2[x]
    somacoluna.append(soma)
    soma = 0
    contc += 1
for y in range(len(somacoluna)):
    print(somacoluna[y],end= " ")