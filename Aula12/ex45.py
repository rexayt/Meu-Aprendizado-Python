from random import randint
print('Bem vindo ao predra papel e tesoura.')
bot = 0
c = 'S'
while c in 'Ss':
    while True:
        op = int(input('Escolha\n -Pedra [1]\n -Papel [2]\n -Tesoura [3]\n----------------\nSua jogada: '))
        bot = randint(1,3)
        if op == 1 and bot == 3:
            print('Você jogou Pedra e o Bot jogou Tesoura, parabéns você ganhou.')
            print('-'*16)
        elif op == 1 and bot == 2:
            print('Você jogou Pedra e o Bot jogou Papel, você perdeu, Loser.')
            print('-'*16)
        elif op == 1 and bot == 1:
            print('Você e o Bot jogaram Papel, Empate')
            print('-'*16)
        if op == 2 and bot == 1:
            print('Você jogou Papel e o Bot jogou Pedra, Parabéns você ganhou.')
        elif op == 2 and bot == 2:
            print('Você jogou Papel e o Bot jogou Papel, Empate.')  
        elif op == 2 and bot == 3:
            print('Você jogou Papel e o Bot jogou Tesoura, Você perdeu.')
        if op == 3 and bot == 1:
            print('Você jogou Tesoura e o Bot jogou Pedra, Você perdeu.')
        elif op == 3 and bot == 2:
            print('Você jogou Tesoura e o Bot jogou Papel, Você ganhou.')
        elif op == 3 and bot == 3:
            print('Você jogou Tesoura e o Bot jogou Tesoura, Empate.')
        break
    c = str(input('Deseja continuar? [S/N]: ')).upper()
    while c not in 'SN':
        c = str(input('Comando inválido digite [S/N]: ')).upper()
