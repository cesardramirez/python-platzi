""" Tuplas y lambda """

"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

"""
    "abacabad"
    {
        'a': (0, 4),  - Muestra el indice donde lo vió la primera vez y cuantas veces aparece esa letra.
        'b': (1, 2),
        'c': (3, 1),
        'd': (7, 1)
    }
"""

def first_not_repeating_char_v2(char_sequence):
    sequence = tuple(char_sequence)

    for char in sequence:
        count_of_char = sequence.count(char)  # Devuelve cuantas veces se repite un caracter en la tupla.
        if count_of_char == 1:
            return char
    
    return '_'

def first_not_repeating_char_v1(char_sequence):
    seen_letters = {}

    # Diccionario de tuplas donde la llave va a ser cada una de las letras y la tupla (indice_primero, num_veces q aparece)
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)
    
    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))  # Lista de tuplas que tiene la letra y el indice donde se encuentra.
    
    # Ordenar la lista de tuplas por el indice.
    # El lambda mencionado es lo mismo que decir def sort_order(value): return value[1]
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]  # Aparece como primer valor la letra que sólo aparece una vez.
    else:
        return '_'  # Indica que todas las letras están repetidas.


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char_v2(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))