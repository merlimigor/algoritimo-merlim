num1=int(input("número termos: "))

y=0

for x in range (1, num1+1):
    print("1/", x)
    y += 1/x

print(y)