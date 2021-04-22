from math import sin, radians, cos, tan
an=float(input('Digite um ângulo: '))
se= sin(radians(an))
print('O ângulo {} tem o seno de {:.2f}'.format(an, se))
co= cos(radians(an))
print('O ângulo {} tem o Cosseno de {:.2f}'.format(an, co))
ta= tan(radians(an))
print('O ângulo {} tem a Tângente de {:.2f}'.format(an, ta))