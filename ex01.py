numeros = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

num_verificar = int(input("Digite um número para verificar se está na lista: "))

if num_verificar in numeros:
    print("O número está na lista!")
else:
    print("O número não está na lista!")