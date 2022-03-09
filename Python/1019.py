duracao = int(input())

hora = duracao // 3600
resto = duracao % 3600
minuto = resto // 60
resto = resto % 60
segundo = resto // 1

print(f'{hora}:{minuto}:{segundo}')
