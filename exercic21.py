#ler 10 valores, calcular e escreve a media aritmetrica desses valores lidos
soma=0
divisão=0
for j in range(10):
    valor=float(input(f"Digite um numero:")) -1
    if valor >=0 and valor <=10:
        soma = soma+valor
        divisao = divisão+1
if divisão!=0:
    media=soma/divisão
    print(f"a media geral é: {media}")
else:
    print("invalido")