cargah = float(input())
if cargah >0:
	if cargah <= 10:
		valor = 50
		bonificacao =500
	elif 20 >= cargah > 10:
		valor = 60
		bonificacao = 600
	elif 30 >= cargah > 20:
		valor = 70
		bonificacao = 700
	else:
		valor = 80
		bonificacao = 800
pagamento = cargah * valor + bonificacao
print(pagamento)
