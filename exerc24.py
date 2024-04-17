#faça um codigo p ler 2 valores e realize a divisao do primeiro e segundo valor recebido
n1=float(input("Digite um numero:"))
n2=float(input("Digite um numero:"))
while n2==0:
    n2 = float(input("numero invalido, digite novamente o numero:"))
resultado= n1/n2
print("resultado:", resultado)

