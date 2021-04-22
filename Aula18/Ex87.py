lista=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um número para [{l}, {c}] : '))
        lista[l][c] = num
        if num % 2 == 0:
            par += num
        if c == 2:
            terceira += num
        if l == 1 and c == 0:
            maior = num
        elif l == 1 and num > maior:
            maior = num
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end=' ')
    print()
print(f'A soma de todos os valores da terceira coluna é {terceira}.')
print(f'A soma de todos os valores pares é {par}.')
print(f'O maior número da segunda linha é {maior}.')
