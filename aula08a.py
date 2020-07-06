#ler um número e calcular a raiz quadrada com a biblioteca
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} vai ser {}'.format(num, raiz))
#posso arredodar a raiz pra cima ou pra baixo
#print('A raiz quadrada de{} vai ser {}'.format (num, math.ceil(raiz)))
#print('A raiz quadrada de{} vai ser {}'.format (num, math.floor(raiz)))