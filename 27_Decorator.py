"""
Un decorador agrega mayor funcionalidad a una función específica.

A, B, C son funciones.
A recibe como parametro B para poder crear C.

- Si envío como parámetro una función es porque necesito que esa función se le agregen más cosas (ya sea antes o después de su ejecución).
- Dentro de nueva_funcion() se va a encargar de ejecutar a la función que recibe como parámetro.
- En la nueva_funcion() debe recibir los parámetros definidos de la función decorada.
  - El *args indica que la función puede recibir n cantidad de argumentos (o parámetros) posicionales.
  - El **kwargs indica que la función puede recibir n cantidad de argumentos (o parámetros) no posicionales sino para un diccionario de argumentos (llave-valor).
  - La palabra args y kwargs se utilizan por convención. Lo realmente importante es definir * y **.
- Un ejemplo de código a agregar antes es abrir una conexión a la BD y el código después es cerrar la conexión a la BD.
- Para decorar una función se coloca encima de la misma el @nombre_decorador.
- En un decorador se pueden enviar parámetros. Para esto, todo el código actual debe estar en una nueva función, cambiar el nombre y en vez de retornar la nueva_funcion() se retornaría la función que tiene el código de todo el decorador.
"""

def decorador(is_valid): # A, B
    def _decorador(func): # A, B (Definición antes de que el decorador recibiera parámetros)
        def before_action():
            # Agregar código antes...
            print('Vamos a ejecutar la función')
        
        def after_action():
            # Agregar código después...
            print('Se ejecutó la función')

        def nueva_funcion(*args, **kwargs):
            if is_valid:
                before_action()
            resultado = func(*args, **kwargs)
            after_action()
            
            return resultado

        return nueva_funcion  # C (Definición antes de que el decorador recibiera parámetros)
    return _decorador  # C

@decorador(is_valid = False)
def saluda():
  print('Hola Mundo')

@decorador(is_valid = True)
def suma(num_1, num_2):
    return num_1 + num_2

saluda()
print(suma(80, 17))