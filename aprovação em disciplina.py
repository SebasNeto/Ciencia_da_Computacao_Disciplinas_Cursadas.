nota = eval(input())
frequencia = eval(input())
cargaHoraria = int(input())
vetorSaida = [0, 0, 0]
for aluno in range(len(frequencia)):
    if frequencia[aluno] >= cargaHoraria * (3/4):
        if nota[aluno] >= 5:
            vetorSaida[0] += 1
        else:
            vetorSaida[1] += 1
    else:
        vetorSaida[2] += 1
print(vetorSaida)
