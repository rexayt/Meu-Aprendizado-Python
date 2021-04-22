def leiaint(msg):
    valor = 0
    ok = False
    n = str(input(msg))
    while True:
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número válido.')
            n = input('Digite um número: ')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')