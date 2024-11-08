#se informado numero negativo o programa para
while True:
   n=int(input('Quer ver a tabuada de qual valor:'))
   print('-'*20)
   if n <0:
       break
   print('-'*20)
   for c in range(1,11):
        print(f'{n}x{c}={n*c}')
   print('-'*20)
print('O programa não informara a tabuada de numeros negativos')
