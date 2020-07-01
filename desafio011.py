#faça um programa que leia a altura e a largura de uma parede em metros, calcule sua area e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinha, pinta uma area de 2 metros quadrados
larg= float(input('Digite a largura da parede em metros:'))
alt = float(input('Digite a altura da parede em metros:'))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintá-la é necessário {}L de tinta .'.format( tinta))


