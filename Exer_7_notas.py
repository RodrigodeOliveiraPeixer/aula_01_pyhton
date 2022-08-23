# 7 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# nota1 = float(input("Digite a primeira nota:"))
# nota2 = float(input("Digite a segunda nota:"))
# nota3 = float(input("Digite a terceira nota:"))
# nota4 = float(input("Digite a quarta nota:"))

# # media = float(nota1+nota2+nota3+nota4)/4 
# # print("A média é :%.1f " % media)

# def notas(nota1,nota2,nota3,nota4):
#     return int( nota1 + nota2 + nota3 + nota4) / 4

# # calculo = float(input("digite a primeira nota : "))
# print(f"A média é :  {notas(nota1,nota2,nota3,nota4)} ")


def pegar_notas():
    media = 0
    for i in range(1,5):
        media += float(input(f"Digite a nota número {i}: "))

    return media / 4


print(pegar_notas())

    


