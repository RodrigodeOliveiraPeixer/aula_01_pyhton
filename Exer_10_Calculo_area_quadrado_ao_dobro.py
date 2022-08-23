# 10 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# comprimento = float(input("Digite a altura do quadrado :"))
# largura = float(input("Digite a largura do quadrado :"))
# area = (comprimento*largura)*2

# print(f"O dobro da área do quadrado é : {area:.0f} m²")



# função

def areadoquadrado(valor):
    A = valor**2
    return A * 2

comprimento = int(input("Digite o comprimento : "))
print(f"O valor do dobro do quadrado é {areadoquadrado(comprimento)} M²")