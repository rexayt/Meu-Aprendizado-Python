km=float(input('Quantos quilómetros ele percorreu? '))
dias=float(input('Quantos dias ele foi alugado? '))
n =(60*dias)+(km*0.15)
print('Seu carro foi alugado por {:.0f} dias, e percorreu {:.2f} quilómetros, custando R${:.2f}'.format(dias, km, n))