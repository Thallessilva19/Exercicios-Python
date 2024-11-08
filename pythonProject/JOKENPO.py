from random import randint
from time import sleep
opcoes=['pedra','papel','tesoura']
pc=randint(0,2)
print('='*20,'JOKENPO','='*20)
print('''Suas opções:
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador= int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-'*20)
print('Computador jogou {}'.format(opcoes[pc]))
print('Jogador jogou {}'.format(opcoes[jogador]))
print('-'*20)
if pc==0: #computador jogou pedra
    if jogador==0:
        print('Empate')
    elif jogador==1:
        print('Jogador venceu')
    elif jogador==2:
        print('Computador vence')
    else:
        print('Jogada invalida')
if pc==1: #computador jogou papel
    if jogador==0:
        print('Computador vence')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('Jogador venceu')
    else:
        print('Jogada invalida')
if pc==2: #computador jogou tesoura
    if jogador==0:
        print('Jogador venceu')
    elif jogador==1:
        print('Computador venceu')
    elif jogador==2:
        print('EMPATE')
    else:
        print('Jogada invalida')
