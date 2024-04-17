#ler 10 valores, calcular e escrever a media aritmetrica desses valores lidos.
soma=0
for j in range(10):
    valor=float(input("Digite o valor:"))
    soma+= valor
    media=soma/10
print("A media aritmetrica dos valores é:", media)