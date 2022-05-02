ordem = int(input())
if ordem >=2:
    while True:
        matriz = []
        for c in range(ordem):
            linha = []
            for j in range(ordem):
                num = int(input())
                linha.append(num)
            matriz.append(linha)
        break
diagonalp = []
for i in range(ordem):
    print(matriz[i][i],end=" ")
    if i == i:
        diagonalp.append(matriz[i][i])
print("")