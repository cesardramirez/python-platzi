import math

def _is_prime_optimized(number):
    """
    Función optimizada. Lo que hará es en vez de recorrer una serie de números (por ejemplo, saber si 1000 es primo o no) lo hace con raíz cuadrada, así el número de comparaciones es menor y hace el programa más eficiente.
    """
    if number < 2:
        return False
    root = int(math.sqrt(number))
    for i in range(2, root + 1):
        if number % i == 0:
            return False
    return True

def _is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True

def run():
    # El pass cuando se coloca en una función indica que en algún momento se le va a poner algo. Esto se hace es para que la función no genere errores porque aún no le hemos definido nada.
    #pass

    number = int(input('Escribe un número: '))
    #result = _is_prime(number)
    result = _is_prime_optimized(number)

    if result:
        print('Tu número es primo.')
    else:
        print('Tu número NO es primo.')

if __name__ == '__main__':
    run()