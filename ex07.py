numeros = []
for i in range(10):
    num = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(num)

print("Números na ordem inversa:")
for num in reversed(numeros):
    print(num)
