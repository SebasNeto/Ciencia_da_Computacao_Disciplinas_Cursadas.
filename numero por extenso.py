d = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
u = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
du = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
c = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
entrada = str(int(input()))
valor = len(entrada)
aspas = ""
for numero in range(-1, -valor - 1, -1):
    if numero == -1 and int(entrada[numero]) != 0:
        aspas = d[int(entrada[numero]) - 1] + aspas
    elif numero == -2 and int(entrada[numero]) not in [0, 1]:
        aspas = du[int(entrada[numero]) - 2] + " e " + aspas
    elif numero == -2 and int(entrada[numero]) == 1:
        aspas = u[int(entrada[numero + 1])]
    elif numero == -3 and int(entrada[numero]) != 0:
        aspas = c[int(entrada[numero]) - 1] + " e " + aspas
    elif numero == -4 and int(entrada[numero]) not in [0, 1]:
        aspas = d[int(entrada[numero]) - 1] + " mil e " + aspas
    elif numero == -4 and int(entrada[numero]) in [0, 1] and valor >= 4:
        aspas =  " mil " + aspas
    elif numero == -5 and int(entrada[numero]) == 1:
        aspas = u[int(entrada[numero]) - 1] + aspas
final = ""
l = aspas.split()
for numero2 in range(len(l)):
    if l[numero2] == "e" and numero2 in [0, len(l)-1]:
        final += ""
    elif numero2 == 0:
        final += l[numero2]
    else:
        final += " " + l[numero2]
if entrada == "100":
    final = "cem"
print(final)