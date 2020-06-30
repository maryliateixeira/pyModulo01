#faça um programa que leia a altura e a largura de uma parede em metros, calcule sua area e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinha, pinta uma area de 2 metros quadrados
alt = float(input('Digite a altura da parede em metros:'))
larg = float(input('Digite a largura da parede em metros:'))
par = alt * larg
tin = par / 2
print('A Area da parede é de {} m²\nSendo necessário {} litros de tinta para pintá-la.'.format(par, tin))
