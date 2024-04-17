#some dois horários determinados e printe a hora resultante
h1= int(input("Digite a hora 1:"))
m1= int(input("Digite os minuto 1:"))
h2= int(input("Digite a hora 2:"))
m2= int(input("Digite os minuto 2:"))
if h1>12:
    h1= h1-12
if h2>12:
    h2=h2-12
hora=h1+h2
minutos=m1+m2
if minutos>=60:
    minutos= minutos-60
    hora= hora+1
print(hora,":",minutos)




