x = []
y = [2, 3, 5, 8, 10]
z = [8, 9, 7, 3, 6]

for n in range(5):
    x.append(y[n] + z[n])

    print(x)
    print()
    print(len(x))
    print()
    max(x)

media = sum(x) / len(x)
print(media)

lista = [3, 7, 8, 9, 1, 12, 4]
lista.sort(reverse=True)
print(lista)

nome = "boll"

l = list(nome)
print(l)

seq = "8796543210"

n = list(seq)
n.sort()
n.append("11")
n.remove("2")
print(n)

l = ["ana", "bruno", "pedro", "maria"]
for nome in l:
    print(f"olá {nome}")
    print()


cidades = []

while True:
    cidade = input("Digite o nome de uma cidade ou 'sair' para encerrar: ").lower()
    if cidade != "sair":
        cidades.append(cidade)
    else:
        break

for cidade in cidades:
    cidades.sort()  
    print(f"Cidades em ordem alfabética: {cidade}")

from random import randint
dado = []

while len(dado) < 6000:
    dado.append(randint(1, 6))
print(dado.count(1)) 
print(dado.count(2)) 
print(dado.count(3)) 
print(dado.count(4)) 
print(dado.count(5)) 
print(dado.count(6)) 