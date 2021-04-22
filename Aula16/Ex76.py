compras=('Pão', 0.75, 
        'Estojo', 3.40,
        'Caderno', 21.35,
        'Notebook', 4555.00,
        'Pedra', 0.00,
        'Fone de ouvido', 120.00)
for c in range(0, len(compras)):
    if c % 2 == 0:
        print(f'{compras[c]:.<30}', end='')
    else:
        print(f'{compras[c]:>2.2f}')