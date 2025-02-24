print("*****Programa para calcular media*****\n\n")

nome = input("Digite o nome do(a)aluno(a):")
nota1 =float(input("Digite a primeira nota:"))
nota2 =float(input("Digite a segunda  nota:"))
nota3 =float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3
if median>=6:
    print(f"O aluno(a){nome} foi aprovado!")
else media = <=5.9:
    print(f"O aluno(a){nome} foi reprovado!")
    print(f"O aluno(a){nome} ficou com a media: {media:.2f}")