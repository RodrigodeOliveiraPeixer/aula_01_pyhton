# 8 - Faça um Programa que converta metros para centímetros.

# metro = int(input("Digite a quantidade de metros:"))
# centimetro = float(metro * 100)
# print(f"{metro} metros é igual a {centimetro:.0f} centimetros")


def conversao(valor): 
    return valor * 100

metro = float(input("Digite a quantidade de metros: "))
print(f"{metro:.0f} metros é igual a {conversao(metro):.0f} centimetros")




