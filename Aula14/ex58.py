import random, time
print('Bem vindo ao meu mundo, meu nome é Jorge o jogador pensativo das profundezas da Darkweb')
time.sleep(2.5)
print('Eu sei, eu sei... Meu nome é grande e estranho porém...')
time.sleep(2)
print('Eu não ligo.')
time.sleep(1.7)
print('Você deve estar se perguntando "O que esse programa faz?"')
time.sleep(2)
print('Eu digo, esse programa é um jogo.')
time.sleep(2)
print('O jogo (perdi kkj), consiste em eu pensar num número, e você advinhar ele, podemos começar?')
time.sleep(2.5)
r = str(input('Qual sua resposta? [S/ N]: ')).strip().upper()
if r == 'S':
    print('Ovo pensar num número, se prepare.')
elif r == 'MACACO':
    print('Essa é uma ótima resposta, MAMACO')
    time.sleep(1)
    print('UH UH UH UH UH UH UH')
    time.sleep(1)
    print('Macaco pensar no número')
elif r == 'N':
    print('Foda-se mermão, vou pensar do msm jeito.')
time.sleep(1)
n=int(random.randint(0, 10))
print('HMMM')
time.sleep(1)
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1.5)
print('Pronto pensei')
time.sleep(1)
j = int(input('Que número eu pensei? (0 - 10): '))
c = 0
while j != n:
    j = int(input('Errastes, tente novamente noob: '))
    c += 1
    if c >= 0 and c <= 3:
        print('Que má sorte em amigão')
    elif c >= 4 and c <= 5:
        print('Tu é muito ruim maluco')
    elif c >= 6 and c <= 7:
        print('MERMÃO PELO AMOR DE DEUS, PARA DE DIGITAR COM A BUNDA')
    elif c >= 8 and c <= 9:
        print('CARALHO MALUCO, É TÃO DIFÍCIL ASSIM ACERTAR UM NÚMERO?????')
    elif c == 10:
        print('Poohta que pariu mlk, tu é horrível, vaza daqui')
    else:
        print('Digita um número decente')
print('Você precisou de {} tentativas.'.format(c))
print('Você ganhou, mas a que custo?')

