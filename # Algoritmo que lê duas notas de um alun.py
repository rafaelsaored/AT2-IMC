# Algoritmo que lê duas notas de um aluno, calcula a média
# e informa se o aluno foi aprovado ou reprovado.
# Notas devem estar entre 0 e 10.
# A média para aprovação é 6.

nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida. Digite uma nota entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida. Digite uma nota entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("Média:", media)

if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")