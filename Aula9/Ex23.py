n1=int(input('Digite um número: '))
a=n1//1%10
b=n1//10%10
c=n1//100%10
d=n1//1000%10
print('Unidade: {}'.format(d))
print('Dezena: {}'.format(c))
print('Centena: {}'.format(b))
print('Milhar: {}'.format(a))