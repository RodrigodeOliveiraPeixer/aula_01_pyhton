# 11 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês.

# def salariomensal(valorh1,valort2):
#     valor = valorh1 * valort2
#     return valor


# valor_hora = float(input("Informe o valor pago por hora : R$  "))
# horas_trabalhadas = float(input("Informe a quantidade de horas : "))
# print(f"O salario à receber é : R$ {salariomensal(valor_hora,horas_trabalhadas):.2f}")


def pegar_valor():
    contador1 = 0
    contador2 = 0
    for i in range(1):
        contador += float(input(f"Digite o valor por pago por hora {i}: "))
    for i in range(1):
        contador += float(input(f"Digite a quantidade de horas {i}: "))    

    return contador 


print(pegar_valor())
