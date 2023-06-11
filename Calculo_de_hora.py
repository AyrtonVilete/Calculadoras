def calcular_valor_hora(salario_mensal, horas_trabalhadas_mes):
    valor_hora = salario_mensal / horas_trabalhadas_mes
    return valor_hora

salario_mensal = float(input("Digite o seu salário mensal: "))
horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

valor_hora = calcular_valor_hora(salario_mensal, horas_trabalhadas_mes)

print("O valor da sua hora de trabalho é:", valor_hora)
