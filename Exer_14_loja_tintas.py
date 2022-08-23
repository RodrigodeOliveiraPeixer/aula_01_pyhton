# 14 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
#  área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 
#  a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    
    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # comprar apenas latas de 18 litros;
    # comprar apenas galões de 3,6 litros;

    # misturar latas e galões, de forma que o desperdício de tinta seja menor.
    # Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#Utilizei comando math para arredondar valores os valores pra cima e não ele considera pra baixo e não fecha a conta

import math

area = int(input("Digite a quantidade de M² deseja pintar : "))

litros = (area / 6) * 1.1
latas = math.ceil(litros / 18)
valor_lata = latas * 80
galao = math.ceil(litros / 3.6)
valor_galao = galao * 25
# utilizei round porque o math não arrenda o valor correto do mix
mixlatas = round(litros / 18)
mixgaloes = round((litros - mixlatas * 18) / 3.6)

if((litros- (mixlatas *18) % 3.6 != 0)):
    mixgaloes += 1
    total_mix = (mixlatas*80) + (mixgaloes * 25)

print(f"Se for usar só latas, você precisará de {latas} lata(s), e custará R$ {valor_lata:.2f}")
print(f"Se for usar só galão, você precisará de {galao} galão(ões), e custará R$ {valor_galao:.2f}")
print(f"Para um melhor custo benefício, você precisará de {mixlatas} lata(s) e {mixgaloes} galão(ões)"
      f"  , e custará {total_mix:.2f}")




