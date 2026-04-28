print("SEJA BEM VINDO AO CINEMA DE ALGORITIMOS E ESTRUTURA DE DADOS")


while True:
    nome = input("Qual seu nome? ")
    idade = int(input("Qual sua idade? "))

    if idade < 16:
        resposta_1 = input("Você está acompanhado? (a entrada só é vendida para menores de 18 anos caso esteja acompanhado) responda sim ou nao\n ")
        if resposta_1 == "nao":
            print("Sinto muito, mas sua entrada foi negada!")
            break
        if resposta_1 == "sim":
            continue
        
    dinheiro = float(input("Qual a quantia de dinheiro que voê tem? "))

    if dinheiro < 30:
        print("Saldo insuficiente")