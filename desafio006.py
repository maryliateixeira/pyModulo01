#crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada
n = int(input('digite um número:'))
print('Analisando o número {}, \no dobro é {},\nO triplo é {}\nE a raíz quadrada {:.2f}' .format(n, (n*2), (n*3), (n**(1/2))))
# a raiz quadrada pode ser calculada pela função pow(n, (1/2)
