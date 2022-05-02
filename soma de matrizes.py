matriza = eval(input("matrizA: "))
linha1 =len(matriza)
coluna1 = len(matriza[0])
matrizb = eval(input("matrizB: "))
liha2 = len(matrizb)
coluna2 = len(matriza[0])
resultado = []
for linha in range(linha1):
    l = []
for coluna in range(coluna2):
    if linha == coluna:
        m = linha * coluna
        l.append(m)
    resultado.append(l)
print(resultado)
