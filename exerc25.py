#faça um codigo para ler a senha de um usuario e apos 3 tentativas erradas
pin=1740
senha=int(input("informe a senha:"))
cont=1
while cont<3:
    if senha==pin:
        print("senha correta:")
        break
    else:
        senha=int(input("senha incorreta, digite novamente:"))
        cont=cont+1
    if cont==3 and senha!= pin:
        print("senha bloqueada:")
        break
