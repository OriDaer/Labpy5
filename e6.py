class Tarea:
    def __init__(self, descripcion, vencimiento):
        self.descripcion = descripcion
        self.vencimiento = vencimiento
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

def agregar_tarea(tareas):
    descripcion = input('Ingrese la descripción de la tarea: ')
    vencimiento = input('Ingrese el número de días para el vencimiento o una fecha de texto: ')
    nueva_tarea = Tarea(descripcion, vencimiento)
    tareas.append(nueva_tarea)
    print('Tarea agregada con éxito.')

def mostrar_tareas(tareas):
    print('\nLista de Tareas:')
    for indice, tarea in enumerate(tareas, start=1):
        estado = 'Completada' if tarea.completada else 'No completada'
        print(f'{indice}. {tarea.descripcion} - {tarea.vencimiento} - {estado}')

def marcar_como_completada(tareas):
    mostrar_tareas(tareas)
    indice = int(input('Ingrese el número de la tarea a marcar como completada: ')) - 1
    if indice >= 0 and indice < len(tareas):
        tareas[indice].marcar_como_completada()
        print('Tarea marcada como completada.')
    else:
        print('Número de tarea inválido.')

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    indice = int(input('Ingrese el número de la tarea a eliminar: ')) - 1
    if indice >= 0 and indice < len(tareas):
        del tareas[indice]
        print('Tarea eliminada con éxito.')
    else:
        print('Número de tarea inválido.')

def main():
    tareas = []
    
    while True:
        print('\nMenú de Opciones:')
        print('1. Agregar Tarea')
        print('2. Mostrar Tareas')
        print('3. Marcar como Completada')
        print('4. Eliminar Tarea')
        print('5. Salir')
        
        opcion = input('Ingrese su opción: ')
        
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            mostrar_tareas(tareas)
        elif opcion == '3':
            marcar_como_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            break
        else:
            print('Opción inválida. Por favor, elija una opción válida.')

if __name__ == '__main__':
    main()
