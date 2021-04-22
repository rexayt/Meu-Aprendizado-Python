gen=str(input('Digite o seu sexo (Masculino/ Feminino): '))
nome=str(input('Digite seu nome: '))
sal=float(input('Digite seu salário: '))
pre=float(input('Digite o preço da casa: '))
an=int(input('Digite em quantos anos voce pretende pagar: '))
prest= pre/(12*an)
trin= sal*0.30
gene= gen.title()
if prest < trin and gene == 'Masculino':
    print('Parabéns Sr. {}, você pode comprar a casa no valor de R${:.2f} em {} anos.'.format(nome, pre, an))
elif prest < trin and gene == 'Feminino':
    print('Parabéns Sra. {}, você pode comprar a casa no valor de R${:.2f} em {} anos.'.format(nome, pre, an))
elif prest > trin and gene == 'Masculino':
    print('Sentimos muito Sr. {}, você não pode comprar a casa no valor de R${:.2f}.'.format(nome, pre))
elif prest > trin and gene == 'Feminino':
    print('Sentimos muito Sra. {}, você não pode comprar a casa no valor de R${:.2f}.'.format(nome, pre))