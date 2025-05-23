def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

indice = calcula_imc(70, 1.80)
print("IMC:", round(indice, 2))
