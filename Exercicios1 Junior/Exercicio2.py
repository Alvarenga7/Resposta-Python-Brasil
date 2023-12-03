#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = float(input("Digite um numero: "))

if num1 < 0:
    print ("Esse numero é negativo")
elif num1 > 0:
    print ("Esse numero é positivo") 
else:
    print ("Esse numero é nulo")    
