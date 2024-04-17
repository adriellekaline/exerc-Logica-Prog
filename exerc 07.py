time1= input("qual o primeiro time")
time2= input("qual o segundo time")

Goltime1= int(input("quantos gol time1 fez"))
Goltime2=int(input("quantos gol time2 fez"))

if Goltime1>Goltime2:
    print(time1, " é vencedor")

elif Goltime1==Goltime2:
    print("ambos empatados")
else:
    print(time2," é o vencedor")

