c = p = r = 0 
while p != 999:
    p = int(input('Digite um número \n[999 para parar] \n Resposta: '))
    if p == 999:
        c += 1
    else:
        r = r + p
        c += 1
if c > 1:
    print('A soma dos {} números deu {}.'.format(c, r))
else:
    print('O número digitado foi {}.'.format(r))