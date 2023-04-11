altura = float(input("Digite sua altura em metros: "))
genero = input("Digite seu gênero (M para masculino ou F para feminino): ")

if genero == "m":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal é", peso_ideal, "kg.")
elif genero == "f":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal é", peso_ideal, "kg.")