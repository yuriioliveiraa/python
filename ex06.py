nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("Lista atual de nomes:", nomes)

indice = int(input("Digite um número de 0 a 4 para remover o nome correspondente: "))

if 0 <= indice < len(nomes):
    removido = nomes.pop(indice)
    print(f"O nome '{removido}' foi removido.")
else:
    print("Índice inválido!")

print("Lista atualizada de nomes:", nomes)