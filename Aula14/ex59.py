import time
C= int(input('Digite um número: '))
C1= int(input('Digite um número: '))
B = True
R = str(' ')
while B == True:
    print('-='*13)
    R = str(input('O que você quer fazer? \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Escolher novos números \n [5] Sair \n Resposta: '))
    time.sleep(1)
    if R == '5':
        print('Você escolheu sair.')
        time.sleep(1)
        B = False
    elif R == '3':
        print('Você escolheu mostrar qual número é maior')
        time.sleep(1)
        if C > C1:
            print('O número {} é maior que o número {}.'.format(C, C1))
        else:
            print('O número {} é maior que o númeor {}.'.format(C1, C))
    elif R == '2':
        print('Você escolheu multiplicar.')
        y = C * C1
        print('A multiplicação de {} por {} é {}.'.format(C, C1, y))
    elif R == '4':
        print('Você escolheu digitar novos números.')
        C = int(input('Digite o novo número: '))
        C1 = int(input('Digite o novo número: '))
    elif R == '1':
        print('Você escolheu somar')
        y = C + C1
        print('A soma de {} e {} é {}.'.format(C, C1, y))
    else:
        print('Comando inválido, digite novamente.')
    print('-='*13)
    time.sleep(1)
print('Fim da transmissão.')
