print("Aula 09")


while True:
    v = (int(input("Digite um valor aqui: ")))

    if v % 5 == 0 and v % 3 == 0:
        print("este numero é divisivivel por 5 e 3")

    else:
        print("Este numero não é divisivel por 5 e 3")


print("Aula 9")

resultado = 0

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

while True:
    c = int(input("Qual o valor da sua compra? "))

    if c > 1001 and c < 5000:
        resultado = c * 0.20
        print(resultado)

    elif c > 5000:
        resultado = c * 0.30
        print(resultado)

    else:
        resultado = c * 0.10
        print(resultado)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


largura = float(input("Digite a largura (em metros): "))
altura = float(input("Digite a altura (em metros): "))

# Cálculos
area = largura * altura
perimetro = 2 * (largura + altura)
diagonal = (largura**2 + altura**2) ** 0.5

# Saída
print("Área:", area, "m²")
print("Perímetro:", perimetro, "m")
print("Diagonal:", diagonal, "m")