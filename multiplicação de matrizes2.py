matriza = eval(input("matrizA: "))
matrizb = eval(input("matrizB: "))
resultado = []
for linha in range(len(matriza)):
    sebas = []
    for coluna in range(len(matrizb[0])):
        soma = 0
        for linha2 in range(len(matriza)):
            soma+= matriza[linha][linha2] * matrizb[linha2][coluna]
        sebas.append(soma)
    resultado.append(sebas)
print(resultado)