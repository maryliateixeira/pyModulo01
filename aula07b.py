n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
su = n1 - n2
print('A soma vale {}, \n  O produto é {} e a Divisão é {:.3f}'.format(s, m, d), end=' ')
print ('A Divisão inteira é {}, a potência é {} e a subtração é {}' .format(di, e, su))
