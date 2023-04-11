n1 = float(input("Digite o numero: "))
n2 = float(input("Digite o numero: "))
n3 = float(input("Digite o numero: "))

menor = n1

if n2 < menor:
    menor = n2
    
if n3 < menor:
    menor = n3
    
print("O menor numero é:", menor)