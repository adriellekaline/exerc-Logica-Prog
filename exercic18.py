# ler os valores e escrever quantos desses valores lidos sao negativos
s=0
for j in range(1,11,1):
    num= int(input("numero: "))
    if num < 0:
        s+=1
print(s)

