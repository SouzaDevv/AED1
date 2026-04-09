numero = input("Digite um número: ")

soma = 0

for digito in numero:
    soma += int(digito)

print("Soma dos dígitos:", soma)

numero = int(input("Digite um número: "))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

soma = 0

while numero > 0:
    soma += numero % 10  
    numero = numero // 10 

print("Soma dos dígitos:", soma)