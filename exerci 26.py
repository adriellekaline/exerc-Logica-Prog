nota1=float(input("Digite a primeira nota:"))
while nota1<0 or nota1>10:
    nota1 = float(input("nota invalida, digite novamente:"))
nota2=float(input("Digite a segunda nota:"))
while nota2<0 or nota2>10:
    nota2 = float(input("nota invalida, digite novamente:"))
media= (nota1+nota2)/2
print(media)