#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere 1 dolar= 5,23 reais
real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 5.50
euro = real / 6.14
print('Com R${:.2f} reais, você pode comprar US${:.2f} dolares e €{:.2f} euros'.format(real, dolar, euro ))

