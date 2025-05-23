from imc import calcula_imc


def classifica_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


imc = calcula_imc(70, 1.80)
print("Classificação:", classifica_imc(imc))
