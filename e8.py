import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    longitud = int(input('Ingrese la longitud deseada para la contraseña: '))
    contraseña = generar_contraseña(longitud)
    print(f'Contraseña generada: {contraseña}')

if __name__ == '__main__':
    main()
