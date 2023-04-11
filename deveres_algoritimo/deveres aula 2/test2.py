quantidade = int(input("Digite a quantidade de números: "))
soma = 0

for i in range(quantidade):
    numero = float(input("Digite o número {}: ".format(i+1)))
    soma += numero

media = soma / quantidade
print("A média aritmética dos números digitados é:", media)