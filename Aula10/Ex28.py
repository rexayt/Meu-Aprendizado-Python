import random
import time
print('PC -Ovo pensar num número aqui, e você tenta advinhar cuau é.')
c=int(random.randint(0, 5))
print('PC -Xo pensar aquie...')
time.sleep(3)
k=int(input('Digite o número que eu pensei: '))
if k == c:
    print('-=-'*14)
    print('PC- Eu pensei no número {} e você no número {}'.format(c, k))
    print('PC- Parabéns, você ganhou, tu é mto brabo mlk.')
    print('-=-'*14)
else:
    print('-=-'*15)
    print('PC- Eu pensei no número {} e você no número {}'.format(c, k))
    print('PC- HA OTÁRIO PERDEU DE MAIS KKKKKKKKKK.')
    print('-=-'*15)