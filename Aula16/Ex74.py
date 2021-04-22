from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior número sorteado foi {max(n)}')
print(f'O menor número sorteado foi {min(n)}')