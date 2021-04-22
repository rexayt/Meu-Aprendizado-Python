from time import sleep
def fatorial(n, show=False):
    """
    :param n: E o numero utilizado para fazer o fatorial
    :param show: Se voce quer ver a formula do fatorial ou não
    :param c: E o numero utilizado no contador
    :param f: E o numero fatorial
    :return: Retorna o valor de F
    """

    f = 0
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
help(fatorial)