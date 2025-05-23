# O que é uma função?
# Uma função é um bloco de código reutilizável que executa uma tarefa específica.

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"IMC calculado {imc:.1f}")

calcula_imc(70, 1.80)