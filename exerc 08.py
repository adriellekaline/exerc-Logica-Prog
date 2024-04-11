combustivel= float (input("quantos litros de combustivel:"))
tipo= input("qual tipo de combustivel:")
if tipo=="E" or tipo== "e":
    valor =combustivel*4.90
    print("voce comprou etanol",valor )
elif tipo== "G" or tipo=="g":
    valor = combustivel * 5.80
    print("voce comprou gasolina", valor)
else:
    print("invalido, combustivel nao aceito")





