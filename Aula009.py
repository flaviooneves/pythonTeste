print('-='*10 +'CALCULO DE EMPRÉSTIMO BANCARIO'+'-='*10)
salario = float(input('Qual o valor do seu salário? '))
casa = float(input('Qual o valor da casa que você quer comprar? '))
anos = float(input('Em quantos anos você quer pagar este empréstimo? '))
meses = anos*12
parcela = casa/meses
print('O valor de sua parcela será {:.2f}'.format(parcela))
if parcela <= (salario * (30/100)):
    print('****Você PODE comprar sua casa!!****')
else:
    print('Você NÃO PODE comprar sua casa. Esse empréstimo é muito alto para o seu salário. ')






















































































