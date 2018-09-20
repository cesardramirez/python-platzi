import random
import os

def run():
    os.system('clear')  # Limpia la pantalla.
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input('Intenta un número (Del 0 al 20): '))

        if number == random_number:
            print('Felicidades! Encontraste el número!')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño...')
        else:
            print('El número es más grande...')


def remain():
    retry = True
    while retry:
        run()
        retry = True if input('Quieres jugar de nuevo? (Y/N): ').upper() == 'Y' else False

if __name__ == '__main__':
    remain()
