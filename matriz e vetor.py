m = eval(input())
vet = eval(input())
resul = []

for c in range(0,5):
    s = 0
    for i in range(6):
        s = s + m[i][c] * vet[i]
    resul.append(s)
print(resul)