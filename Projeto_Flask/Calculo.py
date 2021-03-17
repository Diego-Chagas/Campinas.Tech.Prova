
import time 
print("Olá!Seja muito Bem-vindo(a) A SUA Imobiliária CHAGAS!Por favor selecione o tipo de imóvel que deja adquirir:")
time.sleep(0.5)
print("Vejo que já selecionou o seu imóvel tão desejado!Vamos ao preenchimento ao financiamento:")
time.sleep(0.5)
imovel = float(input('Valor do imóvel: R$'))
salário = float(input('Salário do cliente: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = imovel / (anos * 12)
mínimo = salário * 30/100
print(f"Para pagar o imóvel selecionado de R${imovel} em {anos} anos ",end='')
print(f"A prestação será de {prestação} ao mês")
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
print(f'COMPARANDO tem que pagar {prestação} e o mínimo é de R${mínimo}')