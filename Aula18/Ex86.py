lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
for p in range(0, 3):
    for c in range(0, 3):
        lista[p][c]=int(input(f'Digite um número para {p}, {c}: '))
    print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^6}]', end='')
    print()
print()