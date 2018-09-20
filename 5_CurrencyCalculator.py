def _foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a pesos colombianos.')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

    result = _foreign_exchange_calculator(ammount)

    # La función format() viene a reemplazar la concatenación con un +.
    #  Los {} indica qué parámetro será el colocado según el que se le haya enviado.
    #  {:,} indica que para los decimales, el separador de miles lo hace con una coma.
    print('${} pesos mexicanos son ${:,} pesos colombianos'.format(ammount, result))


if __name__ == '__main__':
    run()
    print('\nFinal')