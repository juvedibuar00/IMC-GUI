print("Módulo IMC importado")

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classifica_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
