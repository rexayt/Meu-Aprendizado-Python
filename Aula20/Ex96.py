from time import sleep
def área():
    print('  Controle de Terrenos  ')
    print('-='*13)
    a = float(input('LARGURA (M): '))
    b = float(input('COMPRIMENTO (M): '))
    print(f'A área de um terreno {a} X {b} é de {a*b}m².')


área()