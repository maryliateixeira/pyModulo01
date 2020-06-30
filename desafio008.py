#escreva um programa que leia o valor em metros o exiba convertido em centímetros e milímetros
num = int(input('Digite o valor, em metros, a ser convertido:'))
cent = num*100
mili = num*1.000
print('Temos então {} metros,\nconvertidos em {:.3f} centímetros \ne {:.3f} milímetros' .format(num, cent, mili))

