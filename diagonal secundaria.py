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
for c in range(ordem):
    print(matriz[c][c])
    if c + c == ordem -1:
        diagonalp.append(matriz[c][c])
    print("")