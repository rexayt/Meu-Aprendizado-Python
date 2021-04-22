#Fazer um programa que leia o ano de nascimento de um atleta, e diga a categoria do atleta.
#Até 9 = Mirim
#Até 14 = Infantil
#Até 19 = Junior
#Até 20 = Sênior
#Acima = Master
from datetime import date
n1=int(input('Digite o ano de seu nascimento: '))
t = date.today().year
m = t - n1
if m <= 9:
    print('Você tem {} anos, sua categoria é Mirim.'.format(m))
elif m <= 14:
    print('Você tem {} anos, sua categoria é Infantil.'.format(m))
elif m <= 19:
    print('Você tem {} anos, sua categoria é Junior.'.format(m))
elif m == 20:
    print('Você tem {} anos, sua categoria é Sênior.'.format(m))
else:
    print('Você tem {} anos, sua categoria é Master.'.format(m))
