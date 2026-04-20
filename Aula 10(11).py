#Lista 1

# print("#Exercici 0")

num = flaot(input("Digite seu numero: "))

if num % 2 == 0:
    print("o numero é par")
else:
    print("O numero é impar")

if num > 0:
    print("Ele é positivo")
elif num < 0:
    print("Ele é negativo")
else: 
    print("ele é zero")

# print("Exercicio 1")

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if num1 > num2:
    print("o numero 1 é maior")
else: 
    print("O numero 2 é maior")

# print("exercicio 2")

num = float(input("Digite o seu valor: "))

if num > 0:
    print(f"O numero é positivo {num}")
else:
    print(f"O numero é negativo {num}")

# print("Exercicio 3")

vogal = ["a", "e", "i", "o", "u"]

letra = input("Digite uma letra: ")

if letra in vogal:
    print("a letra é uma vogal")
else:
    print("É consoante")

# print("Exercicio 4")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7 and media < 9.99:
    print("Aprovado")
elif media == 10.00:
    print("Aprovado com distinção")
else:
    print("Reprovado")

# print("Exercicio 5")

produto1 = float(input("Qual o valor do produto 1: "))
produto2 = float(input("Qual o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro profuto: "))

if produto1 < produto2 and produto1 < produto3:
    print("Escolhe o produto 1, ele custa menos que o produto 2 e 3")
elif produto2 < produto1 and produto2 < produto3:
    print("Escolhe o produto 2, ele custa menos que o produto 1 e 3")
else:
    print("Escolhe o produto 3, ele custa menos que o produto 1 e 3")

# print("Exercicio 6")

n1 = float(input("Insira um número:"))
n2 = float(input("Insira um número:"))
n3 = float(input("Insira um número:"))
if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n1, n2, n3)
    else:
        print(n1, n3, n2)
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(n2, n1, n3)
    else:
        print(n2, n3, n1)
else:
    if n1 >= n2:
        print(n3, n1, n2)
    else:
        print(n3, n2, n1)


# print("Exercicio 7")

curioso = input("Qual periodo vc estuda? (Digite M para matutino; V para vespertino e N para noturno) ")
if curioso == "M":
    print("Bom dia")
elif curioso == "V":
    print("Boa tarde")
else:
    print("Boa noite")



# print("Exercicio 8")

salario = float(input("Digite seu salario: "))

if salario <= 280:
    print("Seu desconto é  de 20%")
elif salario <= 700:
    print("Seu desconto é de 15%")
elif salario <= 1500:
    print("Seu salario é de 10%")
else:
    print("Seu desconto é de 5%")


# print("Exercicio 9")

#Descobrindo o salário bruto
horas_trabalhadas = float(input("Digite a quatidade de horas trabalhadas no mês: "))
valor_horas = float(input("Digite o valor da sua hora: "))

salario_bruto = (horas_trabalhadas * valor_horas)

#Calcular o IR (Imposto de Renda)

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

#Mostrar o desconto do sindicato

sindicato = salario_bruto * 0.03

#Mostrar o valor do Fgts

fgts = salario_bruto * 0.11

#Final

descontos = ir + sindicato
salario_liquido = salario_bruto - descontos

# Resultado
print("Salário Bruto:", salario_bruto)
print("IR:", ir)
print("Sindicato:", sindicato)
print("FGTS:", fgts)
print("Total de descontos:", descontos)
print("Salário Líquido:", salario_liquido)


# print("Exercicio 10")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2 

if media >= 9.0:
    print("Aprovado, parabens você tirou A")
elif media >= 7.5:
    print("Aprovado, Parabens você tirou B")
elif media >= 6.0:
    print("Aprovado, parabens você tirou c")
elif media >= 4.0:
    print("Aprovado, parabens você tirou D")
else:
    print("Reprovado, você tirou E")



# Lista 2

# print("Exercicio 1")

while True:
    try:
        num1 = float(input("Digite um valor de 0 a 10: "))
        if num1 >= 0 and num1 <= 10:
            print("Nota válida", num1)
            break
        else:
            print("Tente denovo, nota inválida")
    except ValueError:
        print("Erro: digite um número válido!")



# print("Exercicio 2")

while True:

    nome = input("Qual seu nome? ")

    senha = input("Digite uma senha ")

    if senha != nome:
        print("Usúsario e senha cadastrados com sucesso")
        break
    else:
        print("tente denovo, sua senha não pode ser igual ao seu nome")


# print("Exercicio 3")

while True:
    nome = input("Nome (mínimo 3 caracteres): ")
    if len(nome) < 3:
        print("Nome inválido")
        continue

    try:
        idade = int(input("Idade (0 a 150): "))
        if idade < 0 or idade > 150:
            print("Idade inválida")
            continue
    except ValueError:
        print("Digite um número válido para idade")
        continue

    try:
        salario = float(input("Salário (> 0): "))
        if salario <= 0:
            print("Salário inválido")
            continue
    except ValueError:
        print("Digite um número válido para salário")
        continue

    sexo = input("Sexo (f/m): ").lower()
    if sexo not in ["f", "m"]:
        print("Sexo inválido")
        continue

    estado_civil = input("Estado civil (s/c/d/v): ").lower()
    if estado_civil not in ["s", "c", "d", "v"]:
        print("Estado civil inválido")
        continue

    print("Dados válidos!")
    break

# 4 - Crescimento populacional

paisA = 80000
paisB = 200000
anos = 0

while paisA < paisB:
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    anos = anos + 1

print("Anos necessários:", anos)


# 5 - Ler 5 números, soma e média

soma = 0

for i in range(5):
    numero = float(input("Digite um número: "))
    soma = soma + numero

media = soma / 5

print("Soma =", soma)
print("Média =", media)



# 6 - Gerador de tabuada

numero = int(input("Digite um número de 1 a 10: "))

print("Tabuada de", numero)

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


# 7 - Série de Fibonacci

n = int(input("Quantos termos deseja ver? "))

a = 1
b = 1

for i in range(n):
    print(a)
    proximo = a + b
    a = b
    b = proximo



# 8 - Média aritmética de N notas

quantidade = int(input("Quantas notas deseja digitar? "))
soma = 0

for i in range(quantidade):
    nota = float(input("Digite a nota: "))
    soma = soma + nota

media = soma / quantidade

print("Média =", media)




# 9 - Tabela de preços

print("Lojas Quase Dois - Tabela de preços")

for i in range(1, 51):
    valor = i * 1.99
    print(i, "- R$", round(valor, 2))



# 10 - Temperaturas

quantidade = int(input("Quantas temperaturas vai digitar? "))

soma = 0

for i in range(quantidade):
    temp = float(input("Digite a temperatura: "))
    
    if i == 0:
        maior = temp
        menor = temp
    
    if temp > maior:
        maior = temp
    
    if temp < menor:
        menor = temp
    
    soma = soma + temp

media = soma / quantidade

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Média:", media)