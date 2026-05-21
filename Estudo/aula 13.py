#Aprendendo sobre funções

'''def mostar_linha():
    print('-' * 30)
print("Título do relatório")
mostar_linha()
print("Descrição do relatório BLA BLA BLA BLAAAAAAAAAAAAAAAA")
mostar_linha()
'''

#Funcao que rececbe um parametro mas não retorna nada

'''def olá(nome):
    print(f"Olá {nome}!")

def mostar_linha():
    print('-' * 30)
olá("Bruno")
print("Título do relatório")
mostar_linha()
print("Descrição do relatório BLA BLA BLA BLAAAAAAAAAAAAAAAA")
mostar_linha()'''

#Funcao que rececbe um parametro e devolve um valor


'''def soma(a, b):
    return a + b
resultado = soma(5, 3)
print(resultado)'''

'''def far(c):
    return (9/5) * c + 32
resultado = (f"{far(30)} °F")
print(resultado)'''


'''def eh_par(n):
    if (n % 2) == 0:
        return True
    else:
        return False
numero = int(input("Digite um número: "))
if eh_par(numero):
    print(f"{numero} é par.")   
else:    
    print(f"{numero} é ímpar.")'''

'''def calcular_imc(peso, altura):
    imc = peso / altura **  2
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
print(f"seu imc é: {imc:.2f}")
classificacao = classificar_imc(imc)
print(f"Classificação: {classificacao}")'''

def eh_primo(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return False
    return True

n = int(input("Digite um valor: "))
if eh_primo(n):
    print(f"o numero {n} é primo")
else:
    print(f"o numero {n} não é primo")
