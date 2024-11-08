n=int(input('Digite um numero inteiro:'))
print('''''Escolha uma das bases para conversão
[1]Converter para octadecimal
[2]Converter para Binario
[3]Converter para Hexadecimal
''')
opção=int(input('Sua opção:'))
if opção==1:
    print('{} para octadecimal é {}'.format(n,oct(n)))
elif opção==2:
    print('{} para binario é {}'.format(n,bin(n)))
elif opção==3:
    print('{} para hexadecimal é {}'.format(n,hex(n)))
else:
    print('Opção invalida')

