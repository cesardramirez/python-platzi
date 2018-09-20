# Función recursiva.
def factorial(number):
    # Caso base.
    if number == 0:
        return 1
    
    return number * factorial(number - 1)

if __name__ == '__main__':
    number = int(input('Escribe un número: '))

    print('{}! : {}'.format(number, factorial(number)))