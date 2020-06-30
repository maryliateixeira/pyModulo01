#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
a = float(input('Digite seu salário:'))
b = 15 * a
c = b / 100
print('O aumento do salário será de {:.3f} porcento' .format(c))
