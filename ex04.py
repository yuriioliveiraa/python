cidades = []

for i in range(3):
    nome_cidade = input(f"Digite o nome da {i+1}ª cidade: ")
    cidades.append(nome_cidade)

print("Lista de cidades cadastradas:")
for cidade in cidades:
    print(f"- {cidade}")