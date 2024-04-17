#Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas desses alunos, no final, mostre amédia aritmética da turma
cont=0
soma=0
estudantes=int(input("digite o numero de estudantes:"))
print()
while cont<estudantes:
    nota=float(input("nota do estudante"))
    cont+=1
    soma=soma+nota
media = soma/estudantes
print(" a media  geral da turma:",media)
