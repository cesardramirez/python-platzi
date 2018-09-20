import sys
print(sys.version)  # Muestra la versión de python en la que se está ejecutando el archivo.
print('')

def funcion_input():
    name = str(input('Cuál es tu nombre?: '))
    print('Hola, ' + name + '!')

#funcion_input()

def conversion_de_datos():
    # De flotante a entero.
    int(4.3)  # 4

    # De entero a flotante.
    float(4)  # 4.0
    print('{:.2f}'.format(3.46712))  # 3.47 - Define cantidad de decimales.

    # De entero a string.
    str(4.3)  # "4.3"

    # De tupla a lista.
    list((4, 5, 2))  # [4, 5, 2]

    # De conjunto a una lista.
    list({3, 2})  # [2, 3]

def operadores_comunes():
    # Longitud para una string, lista, tupla, etc.
    len("key")  # 3

    # Tipo de dato.
    type(4)  # <class 'int'>
    type((5, 2))  # <class 'tuple'>
    type({'llave': 'valor'})  # <class 'dict'>
    type([2, 7]) == tuple  # False

    # Aplicar una conversión a un conjunto.
    # Cada elemento de una lista pasarlo de un entero a un string:
    map(str, [1, 2, 3, 4])  # <map object at 0x7fde4cbc7358>
    # Para visualizarlo se debe convertir a una lista:
    list(map(str, [1, 2, 3, 4]))  # ['1', '2', '3', '4']

    # Redondear un flotante con x número de decimales.
    round(6.3243, 1)  # 6.3

    # Generar un rango en una lista.
    list(range(5))  # [0, 1, 2, 3, 4]
    list(range(5, 40, 3))  # range[inicio, fin, pasos] - [5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]

    # Sumar un conjunto.
    sum([1, 2, 4])  # 7

    # String
    s = 'hola'
    s[0]  # 'h'
    r = 'l' + s[1:]  # 'lola' - Obtiene desde el segundo elemento del string en adelante.
    'tomas' == 'diana'  # False
    'tomas' == 'tomas'  # True - Un string es igual a otro si tienen los mismos caracteres.
    'alberto' < 'zaira'  # True - Compara caracter por caracter en orden alfabético.
    'botella' > 'aldea'  # True
    print(u'niño')  # Toma los caracteres de Unicode (acentos y demás).
    print(r'^')  # Permite que no se excluya ningún tipo de caracter especial.

    my_string = 'platzi'
    my_string = list(my_string)  # ['p', 'l', 'a', 't', 'z', 'i'] - Convierte un string a una lista.
    for i in my_string:
        print(i, end=' ')  # p l a t z i - Imprime todo en una sola línea.
    my_string[4:] = 'os'
    my_string  # ['p', 'l', 'a', 't', 'o', 's']
    my_string = ''.join(my_string)  # 'platos' - Modifica un string por medio de una lista.
    my_string[-1]  # Retorna 's', el último caracter.
    my_string.upper()  # 'PLATZI' - Convierte un string en mayúsculas.
    'PLATZI'.lower()  # 'platzi' - Convierte un string en minúsculas.
    my_string.find('z')  # 4 - Retorna la posición de la letra, -1 si no existe.
    'Esta es mi frase'.split(' ')  # ['Esta', 'es', 'mi', 'frase'] - Separa un string por un caracter específico.
    '2676'.isdigit()  # True
    'Platzi'.startswith('P')  # True
    repr("w'ow")  # '"w\'ow"' - Devuelve la cadena con caracteres escapados.
    'un espacio'.replace(' ', '')  # Reemplaza un caracter de un string.


    # String - List - Slices
    # string[start:end:steps]
    my_string = 'platzi'
    my_string[1]  # 'l'
    my_string[1:]  # 'latzi' - Trae la cadena desde la posición 1 hasta el final.
    my_string[1:3]  # 'la' - Trae la cadena con la posición 1 y 2, pero no la 3. Nunca trae el último valor mencionado.
    my_string[1:6:2]  # 'lti' - Desde la posición 1 al 6, trae los caracteres de 2 en 2.
    my_string[::-1]  # 'iztalp' - Imprime la letra al revés, recorre de derecha a izquierda.
    

    # List
    friends = []  # Forma 1 (Más eficiente) - Inicializar una lista.
    friends = list()  # Forma 2 - Inicializar una lista.
    friends = ['juan', 'pedro', 'estela', 'pepe']
    friends.append('pedro')  # Añadir un elemento al final de una lista.
    friends.extend(['david', 'diana'])  # Añade los elementos de lista a la lista original.
    friends.insert(5, 'daniel')  # Ingresa un elemento en una posición determinada.
    friends.remove('pedro')  # Elimina el primer elemento que coincida de la lista.
    friends.pop(5)  # Elimina un elemento según su índice.
    friends.pop()  # Elimina el último elemento de la lista.
    friends.index('juan')  # Obtiene el índice según su valor. El primero que coincida.
    name == friends.pop()  # Al eliminar el elemento, retorna su valor, por lo cual se puede comparar después.
    name == 'estela'  # True
    del friends[0]  # Elimina un elemento de la lista según su índice.

    nums = [21, 24, 24, 22, 20, 23, 24]
    print(sum(list))  # Suma cada uno de los elementos de la lista.
    nums.sort()  # Ordena una lista de números de menor a mayor.
    sorted([5, 2, 1])  # [1, 2, 5] - Ordena una lista en ese momento sin afectar la original
    
    list_a = [1, 2, 3]
    list_b = [4]
    list_a + list_b  # [1, 2, 3, 4] - Suma el conjunto de listas.
    list_b * 3  # [4, 4, 4] - Replica los elementos de la lista n veces.


    # List - For
    print([2 * i for i in range(5)]  # Manejar un ciclo for en una sola línea y almacenarlo en una lista. [operacion for valor_a_iterar in conjunto_valores]
    print([i+1 if i > 5 else i-1 for i in range(10)])  # Maneja un ciclo for, para que los números mayores a 5 se sume 1, y los que no se reste 1. Siempre debe definirse un else. [operacion if condicion_si else condicion_no for valor_a_iterar in conjunto_valores]
    print('Digite un listado de números enteros separados con un espacio y termine con la tecla Enter: ')
    numbers = [int(i) for i in input().split()]

    # Conocer qué comandos se puede aplicar a un tipo de dato específico.
    dir([5, 2, 1])  # [..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    # Información sobre una función o librería.
    # help([nombre_funcion])
    help(sorted)  # sorted(iterable, key=None, reverse=False). Return a new list containing all items from the iterable in ascending order.


    # Dictionary
    my_dict = {}  # Forma 1 (Más eficiente) - Inicializar un diccionario.
    my_dict = dict()  # Forma 2 - Inicializar un diccionario.
    my_dict['key'] = 'value'  # Asignar un valor según la llave colocada.
    my_dict = {'llave': 'valor'}  # Crear un diccionario ya con llaves y valores fijos.


    # Dictionary - Iterar
    dict_iterate = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # No siempre el resultado será en el mismo orden en que lo escribamos.
    # Retorna sólo las llaves - d b c a
    for key in dict_iterate:
        print(key, end=' ')
    # Retorna sólo las llaves - d b c a
    for key in dict_iterate.keys():
        print(key, end=' ')
    # Retorna sólo los valores - 4 2 3 1
    for value in dict_iterate.values():
        print(value, end=' ')
    # Retorna llave y valor - d 4 b 2 c 3 a 1
    for llave, valor in dict_iterate.items():
        print(llave, valor, end=' ')
    

    # Tuple
    my_tuple = 1, 2, 3, 4  # Se puede definir sin parentesis, aunque la mejor práctica es colocarlas.
    my_tuple = (1, 2, 3, 4)
    my_tuple = (1, )  # La coma indica que se definió una tupla.
    my_tuple += (2, 3, 4)  # (1, 2, 3, 4)


    # Set - Conjunto
    s = set([1, 2, 3])  # {1, 2, 3} - Forma 1 Definicion.
    s = {1, 2, 3}  # Forma 2 Definicion.
    t = set([3, 4, 5])  # {3, 4, 5}
    t = {3, 4, 5}
    type(s)  # <class 'set'> - Parece a un diccionar con un único elemento.

    s.union(t)  # {1, 2, 3, 4, 5} - Union de todos los elementos sin repetir.
    s.intersection(t)  # {3} - Elementos en común de ambos conjuntos.
    s.difference(t)  # {1, 2} - Elementos que son diferentes del segundo conjunto y que no son comunes.
    t.difference(s)  # {4, 5} - Elementos que son diferentes del primer conjunto y que no son comunes.
    s.symmetric_difference(t)  # {1, 2, 4, 5} - Union de conjuntos que no son comunes.
    s.intersection({4})  # set() - Si no encuentra el valor, retorna un conjunto vacío.

    s | t  # {1, 2, 3, 4, 5} - Union
    s & t  # {3} - Intersección.
    s - t  # {1, 2} - Diferencia
    s ^ t  # {1, 2, 4, 5} - Lo inverso a la intersección. Los no comunes.
    
    3 in s  # True - Verifica si el elemento está en el conjunto.
    4 not in s  # False - Verifica si el elemento no está en el conjunto.
    3 in s & t  # True - Verifica que este valor exista en ambos conjuntos.
    3 in s and t  # {3, 4, 5} - Retorna el segundo conjunto si aplica la condicion. Si no está, retorna False.
    3 in t and s  # {1, 2, 3} - Retorna el primer conjunto si aplica la condicion. Si no está, retorna False.

def comprehensions():
    # Recorre un rango de números de 0 a 50 y pregunta... Su residuo es 0? Si es así añade este elemento a la lista.
    pares = [x for x in range(1, 51) if x % 2 == 0]  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
    # Recorre un rango de números de 0 a 50 y pregunta... Su residuo es diferente que 0? Si es así añade este elemento a la lista.
    impares = [x for x in range(1, 51) if x % 2 != 0]  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    # Recorre un rango de números de 0 a 10 y creará un diccionario en donde la llave va a ser el número pero el valor será el cuadrado del número.
    cuadrados = {x: x**2 for x in range(1, 11)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


def add_text_to_string(string, position, text):
    return text.join([string[:position], string[position:]])

print(add_text_to_string('esta bacano este curso', 5, 're'))  # 'esta rebacano este curso'

"""
Clases:
  - Representación de un objeto.
  - Definición: class NombreClase(parametros):
  - Los constructores tienen como nombre __init__ y parámetros self (significa de su misma clase).
"""
class Estudiante(object):
    # Constructor: Método que se llama automáticamente cuando se crea un objeto.
    def __init__(self, nombre_r, edad_r):
        self.nombre = nombre_r
        self.edad = edad_r
        
    def hola(self):
        # El '%s' indica que se pasa un parámetro string y el '%i' indica que se pasa un parámetro entero.
        return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)

#e = Estudiante("Arturo", 21)
#print(e.hola())

def condicion_if():
    a = 3
    b = 5
    c = 4
    if a > b:
        print('{} es mayor que {}'.format(a, b))
    elif a == c:
        print('{} es igual que {}'.format(a, c))
    else:
        print('{} es diferente que {}'.format(b, c))

#condicion_if()

def ciclo_for():
    for i in range(10):
        print(i)

#ciclo_for()  # 0 1 2 3 4 5 6 7 8 9

def ciclo_for_palabra():
    palabra = 'ferrocarril'

    for letra in palabra:
        print(letra, end=' ')

#ciclo_for_palabra()  # f e r r o c a r r i l

def ciclo_for_continue():
    # Si el número no es exactamente divisible entre 3, continua a la siguiente iteración del ciclo.
    for i in range(30):
        if i % 3 != 0:
            continue
        else:
            print(i**2, end=' ')  # Eleva al cuadrado sólo los números que son exactamente divisibles entre 3.

#ciclo_for_continue()  # 0 9 36 81 144 225 324 441 576 729

def ciclo_for_break():
    for i in range(30):
        if i % 3 == 0:
            print(i, end=' ')
        elif i == 22:  # Se sale del ciclo cuando llega al número 22.
            break

#ciclo_for_break()  # 0 3 6 9 12 15 18 21

def ciclo_while():
    x = 0
    while x < 5:
        print(x)
        x += 1

#ciclo_while()  # 0 1 2 3 4