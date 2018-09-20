""" Leer un archivo """

def run():
    """
    El f.readlines() crea una lista y en cada elemento representa una línea del archivo. Utiliza el \n para crear un nuevo elemento.
    Si en el ciclo for se recorre linea por línea, si toma la primera.
    En el open, por defecto se maneja el read o 'r'.
    """
    counter = 0

    with open('el_aleph.txt') as f:
        #print(f.readlines())
        for line in f:
            counter += line.count('Beatriz')
    f.closed

    print('La palabra \'Beatriz\' se encuentra {} veces en el texto.'.format(counter))

if __name__ == '__main__':
    run()