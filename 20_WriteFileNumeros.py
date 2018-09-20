""" Escribir en un archivo """

def run():
    # Si no está el archivo, python lo crea.
    # file es un keyword, por eso colocamos la f.
    # Con el context manager.
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))
    f.closed
    

if __name__ == '__main__':
    run()