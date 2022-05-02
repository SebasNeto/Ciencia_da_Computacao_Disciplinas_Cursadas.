entrada = int(input())
while(entrada > 0):
    if entrada <= 10:
        valor =  50.00
        bonificacao = 500.00
    elif entrada <= 10 or entrada <= 20:
        valor = 60.00
        bonificacao = 600.00
    elif entrada <= 20 or entrada <= 30:
        valor = 70.00
        bonificacao = 700.00
    else:
        valor = 80.00
        bonificacao = 800.00
    break
pagamento = entrada * valor + bonificacao
print(round(pagamento,2))

