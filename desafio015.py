#algoritmo para aluguel de carros, sabendo que o aluguel diario é 60 reais e 15 centavos por km rodado.
dias = int(input('Informe a quantidade de dias alugados:'))
km = float(input('Quantos km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

