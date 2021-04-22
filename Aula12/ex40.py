from time import sleep
import emoji
np1=float(input('Digite a nota da primeira prova: '))
np2=float(input('Digite a nota da sua segunda prova: '))
m=(np1+np2)/2
if m < 5.0:
    print('Sua média foi \033[31m{}\033[m ...'.format(m))
    sleep(1)
    print('\033[32m...\033[m')
    sleep(1.25)
    print('\033[33m......\033[m')
    sleep(1.5)
    print('\033[4;31mCARALHO MLK TU É MTO RUIM DE SERVIÇO TEJE\033[m \033[1;35mR E P R O V A D O\033[m')
elif m >= 5.0 and m <= 6.9:
    print('sua média foi \033[33m{}\033[m '.format(m))
    sleep(1.5)
    print('Parabéns você foi minimamente decente.')
    sleep(1.5)
    print('\033[36mEspero que da próxima vez...\033[m')
    sleep(2)
    print('\033[34mVocê tire uma nota maior que 6.9\033[m')
    sleep(2)
    print(emoji.emojize('\033[35mOu desejará que\033[m \033[7;31mNUNCA\033[m \033[35mtenha feito as provas\033[m :grin:',use_aliases=True))
elif m >= 7.0 and m <= 9.0:
    print('Sua média foi \033[36m{:.1f}\033[m'.format(m))
    sleep(1.5)
    print('\033[036mParabéns você conseguiu ser aprovado\033[m')
    sleep(1.5)
    print('\033[34mVocê pode ir brincar agora.\033[m')
else:
    print('Sua média foi \033[32m{}\033[m'.format(m))
    sleep(1)
    print('Parabéns garoto você foi aprovado')
    sleep(1)
    print('Eu tô tão orgulhoso de você')
    sleep(2)
    print('\033[33mEu vou...\033[m')
    sleep(2)
    print('Te dar um \033[32mPS5\033[m')
