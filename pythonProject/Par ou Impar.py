from random import randint
print('-='*20)
print('PAR OU IMPAR')
print('-='*20)
v=0
while True:
    user=int(input('Diga um valor:'))
    pc = randint(0, 10)
    total=user+pc
    opção=' '
    while opção not in 'PI':
         opção=str(input('P/I?')).upper().strip()[0]
    print(f'Você jogou {user} e o computador jogou {pc} somando {total}')
    print('Deu par'if total%2==0 else'Deu impar',end=' ')
    if opção=='P':
        if total %2==0:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break

    elif opção=='I':
        if total%2==1:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Você venceu {v} vezes.')

