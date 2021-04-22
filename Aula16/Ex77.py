p = ('Paralelepipedo', 'Ricochete', 'Espada',
     'Gigante', 'Paralelogamo', 'Celular', 'Esperar',
     'Jogar')
for c in p:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for x in c:
        if x.lower() in 'aeiou':
            print(x, end=' ')