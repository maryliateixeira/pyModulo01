#faça um algoritmo que leia o preço e mostre seu novo preço, com 5% de desconto.
valor = float(input('Digite o preço do produto R$'))
desconto = valor - (valor* 5/ 100)
print('O produto que custava R${:.2f}, com desconto de 5% custará R${:.2f} reais.' .format(valor, desconto))

