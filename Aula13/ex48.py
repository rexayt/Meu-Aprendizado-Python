soma = 0
cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} números é {}'.format(cont, soma))
