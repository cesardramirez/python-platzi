# Instalar previamente:
#   Python2: sudo apt-get -y install python-tk
#   Python3: sudo apt-get -y install python3-tk

# Ejecutar el programa en la terminal: python [nombre_archivo].py

import turtle

def main():
    window = turtle.Screen()
    david = turtle.Turtle()

    _make_square(david)
    turtle.mainloop()

def _make_square(dave):
    length = int(input('Tamaño de cuadrado: '))
    for i in range(4):
        _make_line_and_turn(dave, length)

def _make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(90)


# Si el nombre del archivo es igual a 'main'
if __name__ == '__main__':
    main()
