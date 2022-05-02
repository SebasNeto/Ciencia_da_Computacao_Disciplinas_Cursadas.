entrada = int(input())
numero = 0
while (entrada >= 2):
    div = 1/entrada
    numero = numero + div
    entrada = entrada - 1
fatorial = 1 + numero
print(fatorial)
