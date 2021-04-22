c = ('\033[m' # 0 -sem cor
     '\033[0;30;41m' # 1 - vermelho
     '\033[0;30;42m' # 2 - verde
     '\033[0;30;43m' # 3 - amarelo
     '\033[0;30;44m' # 4 - azul
     '\033[0;30;45m' # 5 - roxo
     '\033[7;30m'    # 6 - branco 
    ); 
def ajuda(com):
    título(f'Acessando manual do comando\'{com}\'')
    help(com)


def título(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')

#Programa principal
comando=''
while True:
    título('Sistema de ajuda PyHELP')
    comando=str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Mattane')