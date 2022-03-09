idade = int(input())

ano = idade // 365
resto = idade % 365
mes = resto // 30
resto = resto % 30
dia = resto // 1

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
