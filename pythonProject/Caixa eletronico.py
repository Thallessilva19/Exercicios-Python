print('-'*30)
print('Caixa Elétronico')
print('-'*30)
print('Temos cédulas de 50$ 20$ e 1$ ')
valor=int(input('Qual será o valor a ser sacado:'))
total=valor
ced=50
totced=0
while True:
    if total>=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'total de {totced} cedulas de R${ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break
from time import sleep
sleep(1)
print('Transação concluida')