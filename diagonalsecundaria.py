m = []
linha = []
ordem = int(input())
for c in range(0,ordem):
    for i in range(0,ordem):
        linha.append(int(input()))
    m.append(linha)
    linha = []
for a in range(0,len(m)):
    for b in range(0,len(m)):
        if(a+b == ordem -1):
            print(m[a][b], end=" ")