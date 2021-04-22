#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
p = g = c1 = b = c = co = n = me = ca = 0
while True:
    p = str(input('Digite o nome do produto: '))
    b = float(input('Digite o valor do produto: '))
    co += 1
    if b >= 1000:
        c1 += 1
        ca = p
    if co == 1:
        n = b
    else:
        if b < n:
            n = b
            me = p
    g += b
    c = str(input('Você deseja continuar sua compra? [S/ N]: ')).strip().upper()
    while c not in 'SsNn':
        c = str(input('Comando inválido, digite novamente.\n Você deseja continuar sua compra? [S/ N]: '))
    if c in 'Nn':
        break
print(f'O total gasto na compra de {co} produtos é {g}\nO produto com menor valor é {me}, tendo o valor de R$ {n}')
if c1 == 1:
    print(f'Somente um produto é mais caro que R$ 1000,00 e o nome dele é {ca}.')
else:
    print(f'Existem {c1} produtos mais caros que R$ 1000,00')
