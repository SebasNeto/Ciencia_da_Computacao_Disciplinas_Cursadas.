matriza = eval(input("primeira matriz: "))
matrizb = eval(input("segunda matriz: "))
resultado = []

for linhas in range(len(matriza)):
    linha = []
    for colunas in range(len(matriza[0])):
        linha.append(matriza[linhas][colunas] * matrizb[linhas][colunas])
    resultado.append(linha)
print(resultado)
