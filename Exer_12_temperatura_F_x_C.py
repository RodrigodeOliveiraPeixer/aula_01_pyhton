#12-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
        # C = 5 * ((F-32) / 9).


def temperatura(valor):
    conversao = valor - 32
    return conversao / 1.8

temp_fah = float(input("Digite a temperatura em Fahrenheit : "))
print(f"A temperatura em Grau Fahrenheit convertida para Grau celsius é : {temperatura(temp_fah):.1f}°C")