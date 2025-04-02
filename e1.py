p=float(input('ingresa tu peso en kg: '))
a=float(input('ingresa tu altura en metros: '))
# Calcula el IMC
imc= p/(a**2)
print(f'tu imc es {imc}')
if imc >=18.5 and imc < 21 :
    print('tu talla es S')
if imc >=21 and imc < 27 :
    print('tu talla es M')
elif imc >=27 and imc < 31 :
        print('tu talla es XL')
else:
    print('tu talla es XXL')
