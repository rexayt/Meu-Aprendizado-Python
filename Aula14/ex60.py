'''c = int(input('Digite um número: '))
n = c
f = 1
resultado = c
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = {} '.format(f), end='')
    f *= n
    n -= 1'''
c = int(input('Digite um número: '))
n = c
f = 1
for v in range(c, 0, -1):
    print('{}'.format(n), end='')
    print(' X ' if n > 1 else ' = {}'.format(f),end='')
    f *= n
    n -= 1