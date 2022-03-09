def eh_maior(v1, v2, v3):
    maior = 0
    if v1 > v2 and v1 > v3:
        maior = v1
    elif v2 > v3:
        maior = v2
    else:
        maior = v3
    return maior


def eh_menor(v1, v2, v3):
    menor = 0
    if v1 < v2 and v1 < v3:
        menor = v1
    elif v2 < v3:
        menor = v2
    else:
        menor = v3
    return menor


def eh_meio(v1, v2, v3):
    if v1 <= eh_maior(v1, v2, v3) and v1 >= eh_menor(v1, v2, v3):
        meio = v1
    elif v2 <= eh_maior(v1, v2, v3) and v2 >= eh_menor(v1, v2, v3):
        meio = v2
    else:
        meio = v3
    return meio

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
maior = eh_maior(a, b, c)
menor = eh_menor(a, b, c)
meio = eh_meio(a, b, c)

a = maior
b = meio
c = menor

print(a)
print(b)
print(c)

if a >= c + b:
    print('NAO FORMA TRIANGULO')
elif (a**2) == (c**2 + b**2):
    print('TRIANGULO RETANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or c == b or a == c:
        print('TRIANGULO ISOSCELES')
elif a**2 > c**2 + b**2:
    print('TRIANGULO OBTUSANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or c == b or a == c:
        print('TRIANGULO ISOSCELES')
elif a**2 < c**2 + b**2:
    print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or c == b or a == c:
        print('TRIANGULO ISOSCELES')
