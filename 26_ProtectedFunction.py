"""
1. Los decoradores se inicial siempre al ejecutarse un programa.
2. Antes de ejecutar protected_func() ejecuta protected().
3. Recibe de protected_func() la variable password y ejecuta la función wrapper() o envultura.
4. Si se cumple la condicional ejecutará la func() q es igual a protected_func(), sino mostrará un mensaje.
"""
def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func()  # Ejecutar la función que recibimos como parámetro.
        else:
            print('La contraseña es incorrecta')
    
    # Es importante retornarlo como un objeto y no como una función, sino, si se coloca wrapper() se estaría ejecutando esa función nuevamente.
    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    # Esta es la forma que se tendría que definir sin usar decoradores.
    #wrapper = protected(protected_func)
    #wrapper(password)

    # Esta es la forma que se tendría que definir usando decoradores.
    protected_func(password)