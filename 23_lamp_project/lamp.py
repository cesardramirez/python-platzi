# Convención CamelCase.
class Lamp:
    # Variable clase privada.
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    # self: Hace referencia a la propia instancia.
    # __init__: Constructor.
    def __init__(self, is_turned_on):
        # Si empieza con _, indica que es una variable privada.
        self._is_turned_on = is_turned_on
    
    # Método público.
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
    
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()
    
    # Método privado.
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

print('En lamp.py __name__ es:', __name__)

if __name__ == '__main__':
    print(__name__)