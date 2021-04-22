n1 = 0
cont = 0
for c in range(1, 6+1):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        n1 += n
        cont += 1
if n1 % 2 == 0 and cont == 1:
    print('Você digitou {} número par e o resultado é {}.'.format(cont, n1))
elif n1 % 2 == 0 and cont >= 2:
    print('Você digitou {} números pares e a soma total foi {}.'.format(cont, n1))
else:
    print('Deu ruim fiato')