from time import sleep

def fore(i, f, p):
    """
    Programa utilizado para fazer contagens especificadas pelo usuario.
    :param i: Variavel utilizada para informar o Início da contagem (Início)
    :param f: Variavel utilizada para informar o número final da contagem (Final)
    :param p: Variavel utilizada para informar o número utilizado para pular a contagem (Passo)
    :return: Sem retorno
    """
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if c <= 0:
        c = 1
    for m in range(i, f+1, p):
        print(m, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-='*20)

help(fore)