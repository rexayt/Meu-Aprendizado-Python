número = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
r = int(input('Digite um número de 0 - 20: '))
while r >= 21 or r <= -1:
    r=int(input('Número inválido digite um número de 0 - 20: '))
print(f'O número digitado foi {número[r]}')