matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for linha in range(0,6):
    for coluna in range(0,5):
        matriz[linha][coluna] = int(input([linha,coluna]))
print(matriz)