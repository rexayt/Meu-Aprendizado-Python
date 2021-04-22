t = int (input('Quantos termos você quer mostrar? '))
c = 1
v = 0
f = 1
x = 0
while c < t+1:
    print('-> {}'.format(x), end=' ')
    if c == t:
        print('-> ', end='')
    x = v + f
    v = f
    f = x
    c += 1
print('Fim')