num1 = int(input("Digite um número inteiro: "))

resultado = 1
for i in range(1, num1+1):
    resultado *= i

print(f"O fatorial de {num1} é: {resultado}")