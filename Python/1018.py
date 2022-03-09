valor = int(input())

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
notas1 = resto // 1

print(f'{notas100:.0f} nota(s) de R$ 100,00')
print(f'{notas50:.0f} nota(s) de R$ 50,00')
print(f'{notas20:.0f} nota(s) de R$ 20,00')
print(f'{notas10:.0f} nota(s) de R$ 10,00')
print(f'{notas5:.0f} nota(s) de R$ 5,00')
print(f'{notas2:.0f} nota(s) de R$ 2,00')
print(f'{notas1:.0f} nota(s) de R$ 1,00')
