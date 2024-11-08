
print('=-'*20)
print('SIMULADOR DE EMPRESTIMOS')
print('=-'*20)
casa=float(input('Qual o valor da casa do seu interesse?'))
salario=float(input('Qual a sua renda:'))
ano=int(input('Em quantos meses pretende pagar o seu emprestimo:'))
parcela=casa / (ano*12)
p2=salario*30/100
if parcela<=p2:
      print('PARABENS!! A parcela ficou {:.2f}'.format(parcela))
else:
    print('Que pena, seu emprestimo foi negado a parcela de {} ficou maior que 30% da sua renda'.format(parcela))




