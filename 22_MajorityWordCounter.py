from collections import Counter
import re

"""
La librería o módulo 're' es para el manejo de expresiones regulares.
El método findAll() devuelve una lista de elementos según la expresión regular que se haya definido. En nuestro caso 4567 elementos de palabras (incluso repetidas).
El '\w' indica que coincide con cualquier carácter alfanumérico o guión bajo en el conjunto [a-zA-Z0-9_].
El '+' indica la aparición de 1 o más coincidencias de esa palabra (y que no lo separe por letras).
El método most_commont() del módulo Counter genera una lista de tuplas. En cada tupla va a estar la palabra y el número de veces que aparece esta palabra en la lista 'words'. En este caso mostrará sólo las 5 primeras concurrencias.
"""

words = re.findall(r'\w+', open('el_aleph.txt').read().lower())
print(Counter(words).most_common(5))