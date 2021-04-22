from datetime import date
print('Olá este programa serve para você analisar se um ano específico é bissexto ou não.')
n=int(input('Por favor, digite o ano que você deseja analisar: '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano de {} é Bissexto.'.format(n))
else:
    print('O ano de {} não é Bissexto'.format(n))
