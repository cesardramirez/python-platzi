# -*- coding: utf-8 -*-
# Instalar previamente:
#   Python2: sudo apt-get -y install python-tk
#   Python3: sudo apt-get -y install python3-tk

# Ejecutar el programa en la terminal: python [nombre_archivo].py

import turtle  # Módulo para generar programas gráficos.

window = turtle.Screen()  # Genera una ventana.
david = turtle.Turtle()
david.forward(50)  # Traza una línea.
david.left(90)  # Gira a la izq en 90 grados.

david.forward(50)
david.left(90)

david.forward(50)
david.left(90)

david.forward(50)
david.left(90)

turtle.mainloop()  # Permite no cerrar la ventana.