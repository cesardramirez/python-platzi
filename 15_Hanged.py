""" Listas """

import random

# ASCII ART
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word_v2():
    return random.choice(WORDS)

def random_word():
    index = random.randint(0, len(WORDS))
    return WORDS[index]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print(''.join([' --- *'] * 6))

def validate_sucess_v3(hidden_word):
    """
    Convierte la lista en un string y valida que no exista el caracter '-1'. Retorna -1 si no lo encuentra.
    """

    return True if ''.join(hidden_word).find('-') == -1 else False 

def validate_sucess_v2(hidden_word):
    """
    Revisa en la lista que no exista un elemento específico.
    """

    return True if not '-' in hidden_word else False

def validate_sucess_v1(hidden_word):
    """
    Al intentar ejecutar la instrucción de index y no muestra el valor, no arrojará -1 sino ValueError: '-' is not in list.
    Por lo cuál, cuando pase esta excepción definiremos nuestras instrucciones.
    """

    try:
        hidden_word.index('-')
    except ValueError:
        return True

def run():
    word = random_word_v2()
    hidden_word = ['-'] * len(word)
    tries = 0

    while tries < len(IMAGES) - 2:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for index in range(len(word)):
            if word[index] == current_letter:
                letter_indexes.append(index)
        
        if len(letter_indexes) == 0:
            tries += 1

            if tries == len(IMAGES) - 2:
                display_board(hidden_word, tries)
                print('\n¡Perdiste! La palabra correcta era {}'.format(word))
        else:
            for index in letter_indexes:
                hidden_word[index] = current_letter
        
        if validate_sucess_v3(hidden_word):
            print('\n¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
