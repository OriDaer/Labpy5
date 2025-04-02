import random
numRandom=random.randint(1,100)
n=0
print(numRandom)
userNum= int(input('ingrese un numero aleatorio para adivinar: '))
while (userNum!=numRandom):
    n+=1
    if userNum<numRandom:
        print('el numero que ingresaste es menor que el numero aleatorio')
        userNum= int(input('ingrese un numero aleatorio para adivinar: '))
    if userNum>numRandom:
        print('el numero que ingresaste es mayor que el numero aleatorio')
        userNum= int(input('ingrese un numero aleatorio para adivinar: '))
if userNum==numRandom:
    print(f'felicidades adivinaste el numero aleatorio en {n} intentos')