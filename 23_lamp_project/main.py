""" Definición de clases y objetos / Importar módulos """

# from [modulo] import [clase]
from lamp import Lamp

def run():
    lamp = Lamp(is_turned_on=False)
    #lamp = Lamp(True)  No se utiliza por convención, ya que no indica a que variable se está asignando.

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

"""
- Cuando se ejecuta 'python3 lamp.py' mostrará dos veces el resultado de __main__ para la variable __name__. Esto pasa es porque el módulo principal que estamos ejecutando es la misma clase principal.
- Por el contrario, si ejecutamos 'python3 24_LampMain.py' mostrará el resultado de lamp para la variable __name__. Por qué esta vez no muestra como valor __main__? Porque realmente el módulo principal que estamos ejeutando es 24_LampMain.py y no 'lamp.py'. Por eso, en lamp.py no se ejecuta las instruciones difinidas en el if mientras que en 24_LampMain.py si, por eser esta la función principal.
"""
if __name__ == '__main__':
    run()