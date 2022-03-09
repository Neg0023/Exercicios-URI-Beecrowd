v1, v2, v3 = input().split()
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)
maior = 0
menor = 0
meio = 0
if v1 > v2 and v1 > v3:
    maior = v1
elif v2 > v3:
    maior = v2
else:
    maior = v3

if v1 < v2 and v1 < v3:
    menor = v1
elif v2 < v3:
    menor = v2
else:
    menor = v3

if v1 < maior and v1 > menor:
    meio = v1
elif v2 < maior and v2 > menor:
    meio = v2
else:
    meio = v3
print(menor)
print(meio)
print(maior)
print()
print(v1)
print(v2)
print(v3)
