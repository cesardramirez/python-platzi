# Instalar previamente:
#   Python2: sudo apt-get -y install python-tk
#   Python3: sudo apt-get -y install python3-tk

# Ejecutar el programa en la terminal: python [nombre_archivo].py

import turtle

def main():
    window = turtle.Screen()
    david = turtle.Turtle()
    
    _draw_figure(david)
    turtle.mainloop()

# Por convención, cuando se define una función que llama un método y se encuentra en el mismo archivo, se coloca el _.
def _draw_figure(dave):
    length = int(input("Length: "))
    sides = int(input("Sides: "))

    while sides < 3:
        sides = int(input("The minimun number of sides are 3.\nSides: "))

    angle = 360 / sides

    for i in range(sides):
        dave.forward(length)
        dave.left(angle)


if __name__ == '__main__':
    # Indica cuál es el método que se va a ejecutar primero al iniciarlo desde la consola.
    main()
