print('Parabéns você foi escolhido para ter um aumento, por favor me diga seu salário.')
s=float(input('Digite o seu salário: '))
if s >= 1250.00:
    au=(0.1*s)+s
    print('Seu salário irá aumentar em 10%, ficando no total R${:.2f}, parabéns.'.format(au))
else:
    au1=(0.15*s)+s
    print('Seu salário irá aumentar em 15%, ficando no total R${:.2f}, parabéns.'.format(au1))