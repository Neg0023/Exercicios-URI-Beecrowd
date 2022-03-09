cod, qtd = input().split()
cod = int(cod)
qtd = int(qtd)

if cod == 1:
    valor = 4.00
elif cod == 2:
    valor = 4.50
elif cod == 3:
    valor = 5.00
elif cod == 4:
    valor = 2.0
elif cod == 5:
    valor = 1.50

total = qtd * valor
print(f'Total: R$ {total:.2f}')
