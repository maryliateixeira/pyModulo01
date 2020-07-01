#escreva um programa que leia o valor em metros o exiba convertido em centímetros e milímetros
medida = float(input('Digite uma distancia, em metros, a ser convertido:'))
cm = medida*100
mm= medida*1000
dm = medida*10
dam = medida/10
hm = medida/100
km = medida/1000
print('Temos então {} m,\nconvertidos em {:.3f} cm \n {:.3f} mm \n {:.3f} dm \n {:.3f} dam \n {:.3f} hm \n {:.3f} km ' .format(medida, cm, mm, dm, dam, hm, km))


