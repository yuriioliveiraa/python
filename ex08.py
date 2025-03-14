numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

print("Números e suas posições na lista:")
for i, num in enumerate(numeros):
    print(f"Posição {i}: {num}")
