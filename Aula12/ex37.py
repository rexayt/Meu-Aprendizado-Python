num = int(input('Digite um número inteiro para ser convertido: '))
op = int(input('Digite a opção que você quer\n-Decimal [1]\n-Octal [2]\n-Hexadecimal[3]\nSua escolha: '))
if op == 1:
    print(f'A opção escolhida foi Decimal, logo {num} convertido para Decimal fica {bin(num)}')
elif op == 2:
    print(f'A opção escolhida foi Octal, logo {num} convertido para Octal fica {oct(num)}')
elif op == 3:
    print(f'A opção escolhida foi Hexadecimal, logo {num} convertido para Hexadecimal fica {hex(num)}')