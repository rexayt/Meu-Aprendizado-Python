from math import hypot
co=float(input('Digite o valor Cateto Oposto: '))
ca=float(input('Digite o valor Cateto Adjacente: '))
hip=hypot(ca, co)
print('A hipotenusa vale {:.2f}'.format(hip))