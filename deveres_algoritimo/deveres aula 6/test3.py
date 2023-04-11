num1 = int(input("Número de termos: "))
b = 3
h = 1/1
if num1>=1:
    print(("{}/{}").format(1, 1))
for x in range(2, num1+1):
    print(("{}/{}").format(x, b))
    h += x/b
    b += 2
print(("%.2f") %(h))