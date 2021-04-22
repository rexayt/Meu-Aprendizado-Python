n=float(input('Digite a distância da sua viagem: '))
v=n*0.50
m=n*0.45
if n <= 200:
    print('Sua viagem tem {:.0f} KMs e o valor cobrado será R$ {:.2f}.'.format(n, v))
else:
    print('Sua viagem tem {:.0f} KMs e o valor cobrado será R$ {:.2f}'.format(n, m))
