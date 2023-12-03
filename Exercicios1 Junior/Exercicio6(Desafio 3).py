num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 < num2:
    print("O primeiro numero é o menor", num1)


elif num2 < num1:
    print("O segundo numero é o menor", num2)


elif  num3 < num1 or num2:
    print("O terceiro numero é o menor: ", num3)

