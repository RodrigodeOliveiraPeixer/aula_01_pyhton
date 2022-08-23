altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))
IMC = peso / altura **2
print("Seu IMC é: %.2f"  % IMC )

if IMC < 18.5:
    print("Você está abaixo do peso!")
elif IMC < 24.9:    
    print("Parabéns! você está no peso ideal.")  
elif IMC < 29.9:
    print("você está com Sobrepeso!") 
elif IMC < 39.9:
    print("Cuidado! você está com obesidade.") 
else:
    print("você está com obesidade grave! Procure um médico.")    




    # 0- Crie uma aplicação que calcule o IMC do indivíduo, pesquise a fórmula e aplique.    