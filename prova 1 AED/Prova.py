print("SEJA BEM VINDO AO CINEMA DE ALGORITIMOS E ESTRUTURA DE DADOS")

while True:
    try:

        nome = input("Qual seu nome? ")
        idade = int(input(f"Qual sua idade {nome}? "))

        if idade <= 16:
            resposta_1 = input(f"Você está acompanhado {nome} ? (a entrada só é vendida para menores de 18 anos caso esteja acompanhado) responda sim ou nao\n ")
            if resposta_1 == "nao":
                print("Sinto muito, mas sua entrada foi negada!")
                break

            if resposta_1 == "sim":
                print("otimo")
            
        dinheiro = float(input("Qual a quantia de dinheiro que voê tem? "))

        if dinheiro < 30:
            print(f"Saldo insuficiente {dinheiro}")
        else:
            filme = input("Qual filme você vai asssitir? ")
            print(f"Otima escolha, o filme {filme} é muito falado, efim, ingresso comprado viu!!!! OTIMO FILME")

        desejo = input("Deseja continuar? (s/n)")
        if desejo == "n":
            break 

    except ValueError:
        print("Tente denovo!")
        