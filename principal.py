import imc  # Importa o módulo inteiro

indice = imc.calcula_imc(70, 1.75)
classificacao = imc.classifica_imc(indice)

print(f"IMC: {indice:.2f}")
print(f"Classificação: {classificacao}")
