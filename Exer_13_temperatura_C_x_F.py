# 13 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def temperatura(valor):
    conversao = valor * 1.8
    return conversao + 32

temp_cel = float(input("Digite a temperatura em Grau Celsius : "))
print(f"A temperatura em Grau celsius convertida para Grau Fahrenheit é : {temperatura(temp_cel):.1f}°F")