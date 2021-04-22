c = 3
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite outro número: ')))
print(f'Você digitou os números: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if c in n:
    print(f'O número 3 apareceu na {n.index(3)+1} posição')
else:
    print('O número 3 não foi digitado.')
for c in n:
    if c % 2 == 0:
        print(n, end='')