altura = float(input("Digite sua altura (ex: 1.75): "))
sexo = input("Digite seu sexo (M para masculino / F para feminino): ").upper()

if sexo == "M":
    peso = (72.7 * altura) - 58
elif sexo == "F":
    peso = (62.1 * altura) - 44.7
else:
    print("Sexo inválido!")
    exit()

print(f"Seu peso ideal é: {peso:.2f} kg")