from random import randint
b = j = m = p = c = 0
while True:
    b = int(randint(0, 10))
    j = int(input('Digite um número: '))
    p = str(input('Digite Par ou Impar: [P/ I] ')).upper().strip()
    m = b + j
    if p in 'Pp':
        if m % 2 == 0:
            c += 1
        else:
            break
    if p in 'Ii':
        if m % 2 == 1:
            break
        else:
            c += 1
print(f'Você ganhou {c} vezes.')
