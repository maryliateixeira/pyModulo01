#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere 1 dolar= 5,23 reais
real = float(input('Quantos reais voce tem na carteira?'))
dolar = float(input('Qual a cotação do dolar?'))
result = real/dolar
print('Com a cotação em R${}, voce possui R${} reais, que é o equivalente a US${} dolares.' .format(dolar, real, result ))
