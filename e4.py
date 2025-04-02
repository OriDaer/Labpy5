# Validador de contraseña:
import string

contraseña=input('ingresa constraseña: ')

def verficaContaseña(contraseña):
    May=0
    min=0
    dig=0
    esp=0
    caract=0
    for i in contraseña:
        if len(contraseña)>=8:
            caract+=1
            #print('tiene 8 caracteres')
        if i.isupper() and May==0:
            May+=1
            #print('Mayusc')
        if i.islower() and min==0:
            min+=1
            #print('Minuscula')
        if i.isdigit() and dig==0:
            dig+=1
            #print('Digito')
        if i in string.punctuation and esp == 0:
            esp+=1
            #print("tiene un caracter especial")
    if caract==1 and May==1 and min==1 and dig==1 and esp==1:
        print('Contraseña valida')
    else:
        print('Contraseña invalida')

verficaContaseña(contraseña)