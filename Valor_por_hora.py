valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print("Salário Bruto: R$", salario_bruto)
print("Descontos:")
print(" - Imposto de Renda (11%): R$", imposto_renda)
print(" - INSS (8%): R$", inss)
print(" - Sindicato (5%): R$", sindicato)
print("Salário Líquido: R$", salario_liquido)
