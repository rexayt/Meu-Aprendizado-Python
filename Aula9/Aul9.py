''''frase=('Curso em vídeo Python')
print(frase[0:21:2])
print(frase[:5])
print(frase[13:])
print(frase[9::3])'''
#[]= isso representa uma lista
'''frase=('Curso em vídeo Python')
print(len(frase))
print(frase.count('u'))
frase=('Curso em vídeo Python')'''
#count = serve para contar quantos (letra ou número) tem na string ou conta etc etc
'''print(frase.count('o', 0, 14))
frase=('Curso em vídeo Python')'''
#find = achar algo dentro de uma frase e a mesma te retorna o número onde ela começa, se nao tiver ele
#manda um número -1
'''print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
frase=str('Curso em vídeo Python')'''
#replace = trocar palavras
'''print(frase.replace('Python','Android'))'''
#upper = transformar a frase em maiúscula
'''print(frase.upper())'''
#lower = assim com upper o lower transforma as letras em minúsculas
'''print(frase.lower())'''
#captlize = joga todas as letras em minúscula e deixa apenas a primeira letra em maiúscula
'''print(frase.capitalize())'''
#title = transforma todo o começo de palavra em maiúscula
'''print(frase.title())''' 
'''frase=('  Aprenda Python  ')
print(frase)'''
#strip = tira todos os espaços inúteis
'''print(frase.strip())'''
#rstrip = é uma variaçao de strip que tira apenas os espaços da direita
'''print(frase.rstrip())'''
#lstrip = mesma coisa que rstrip porém é apenas na esquerda
'''print(frase.lstrip())
frase=('Curso em vídeo Python')'''
#split = serve para dividir uma frase e tornar ela uma lista indivídual a cada espaço
'''print(frase.split())
r=frase.split()'''
#join = serve para colocar algo entre os espaços
'''print('-'.join(r))'''