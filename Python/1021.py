valor = float(input())

notas100 = valor // 100
resto = valor % 100
notas50 = resto // 50
resto = resto % 50
notas20 = resto // 20
resto = resto % 20
notas10 = resto // 10
resto = resto % 10
notas5 = resto // 5
resto = resto % 5
notas2 = resto // 2
resto = resto % 2
moeda1 = resto // 1
resto = resto % 1
moeda50 = resto // 0.50
resto = resto % 0.5
moeda25 = resto // 0.25
resto = resto % 0.25
moeda10 = resto // 0.10
resto = resto % 0.10
moeda5 = resto // 0.05
resto = resto % 0.05
moeda01 = resto / 0.01

print('NOTAS:')
print(f'{notas100:.0f} nota(s) de R$ 100.00')
print(f'{notas50:.0f} nota(s) de R$ 50.00')
print(f'{notas20:.0f} nota(s) de R$ 20.00')
print(f'{notas10:.0f} nota(s) de R$ 10.00')
print(f'{notas5:.0f} nota(s) de R$ 5.00')
print(f'{notas2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda1:.0f} moeda(s) de R$ 1.00')
print(f'{moeda50:.0f} moeda(s) de R$ 0.50')
print(f'{moeda25:.0f} moeda(s) de R$ 0.25')
print(f'{moeda10:.0f} moeda(s) de R$ 0.10')
print(f'{moeda5:.0f} moeda(s) de R$ 0.05')
print(f'{moeda01:.0f} moeda(s) de R$ 0.01')
