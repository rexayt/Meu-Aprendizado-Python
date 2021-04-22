def voto(a=0):
    from datetime import datetime    
    b = datetime.now().year - a
    if b <= 15:
        print(f'Com {b} anos, você não está apto para votar.')
    elif b >= 16 and b <= 17 or b >= 65:
        print(f'Com {b} anos, seu voto é opcional.')
    elif b >= 18:
        print(f'Vá votar, com {b} anos seu voto é obrigatório.')


a = int(input(f'Digite o ano de seu nascimento: '))
voto(a)