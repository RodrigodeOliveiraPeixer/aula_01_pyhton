# 9 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# raio = float(input("Digite o raio do círulo :"))
# area = (raio**2)*3.14

# print(f"A área do círculo é : {area:.2f}")

# FUNÇÃO

def areadocirculo(valor):
    A = valor**2
    return A * 3.14

raio = float(input("Digite o raio : "))
print(f"A área do círculo é {areadocirculo(raio)} ")


