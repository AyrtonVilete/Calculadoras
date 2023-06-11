def calcular_peso_ideal(altura, genero):
    if genero == "homem":
        peso_ideal = (72.7 * altura) - 58
    elif genero == "mulher":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        return "Gênero inválido."

    return peso_ideal

altura = float(input("Digite a altura em metros: "))
genero = input("Digite o gênero (homem ou mulher): ")
peso = float(input("Digite o seu peso em kg: "))

peso_ideal = calcular_peso_ideal(altura, genero)

if peso < peso_ideal:
    print("Seu peso está abaixo do peso ideal. O peso ideal é:", peso_ideal, "kg")
elif peso > peso_ideal:
    print("Seu peso está acima do peso ideal. O peso ideal é:", peso_ideal, "kg")
else:
    print("Seu peso está no peso ideal.")