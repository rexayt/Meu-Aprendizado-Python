ma = me = 0
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para entrar na posição {c}: ')))
    if c == 0:
        ma = me = lista[c]
    else:
        if lista [c] > ma:
            ma = lista[c]
        if lista[c] < me:
            me = lista[c]
print(f'O maior número digitado foi {ma} nas posições ', end='')
for i, v in enumerate(lista):
    if v == ma:
        print(f'{i}, ', end='')
print('.')
print(f'O menor número foi {me} nas posições ', end='')
for i, v in enumerate(lista):
    if v == me:
        print(f'{i}, ', end='')
print('.')