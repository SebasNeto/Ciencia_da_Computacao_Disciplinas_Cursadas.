VetA = eval(input("Alunos: "))
VetB = eval(input("nota disciplina B: "))
VetC = eval(input("notas disciplina C: "))
VetD = []
for aluno in range(len(VetA)):
    VetD.append((VetB[aluno]+VetC[aluno])/2)
for aluno in range(len(VetA)):
    print("Aluno: ",VetA[aluno],"-","media: ",VetD[aluno])
    