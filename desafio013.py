#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu salário R$'))
aumento = salario + (salario * 15 / 100)
print('O salário é R${:.2f} e com o aumento de 15% será R${:.2f} reais' .format(salario, aumento))
