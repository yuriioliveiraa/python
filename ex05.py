numeros = [3, 7, 12, 18, 25, 30, 42, 56, 67, 89]

num_verificar = int(input("Digite um número para verificar se está na lista: "))

if num_verificar in numeros:
    print("O número está na lista!")
else:
    print("O número não está na lista!")
