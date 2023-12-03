numero = 7
contador = 0

for n in range(2, numero):
    if numero % n == 0:
        contador = contador + 1

else:    
        print(f"{numero} é primo." if contador == 2 else f"{numero} não é primo")
