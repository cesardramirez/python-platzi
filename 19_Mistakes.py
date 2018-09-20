""" Excepciones """

countries = {
    'mexico' : 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

flag = True

while flag:
    country = str(input('Escribe el nombre de un país: ')).lower()

    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
    except Exception as e:
        print(type(e).__name__)
        print('No tenemos el dato de la población de {}'.format(country))
        flag = False