''''''''''''''''''''''''''''''''''''''''''''''''
import random

numero_secret = random.randint(1, 10)

while True:
    try:
        print("Qual numero voce está pensando? ")
        num_escolhido = int(input(""))

        if num_escolhido < numero_secret:
            print("o numero é maior")

        elif num_escolhido > numero_secret:
            print("o numero é menor")

        else:
            print("Voce acertou!!!!!!!!")
            break

    except ValueError:
        print("Tente denovo!")

''''''''''''''''''''''''''''''''''''''''''''''''
import random

numero_secret = random.randint(1, 10)

while True:
    try:
        print("Qual numero voce está pensando? ")
        num_escolhido = int(input(""))

        if num_escolhido < numero_secret:
            print("o numero é maior")

        elif num_escolhido > numero_secret:
            print("o numero é menor")

        else:
            print("Voce acertou!!!!!!!!")
            break

    except ValueError:
        print("Tente denovo!")

''''''''''''''''''''''''''''''''''''''''''''''''
    


