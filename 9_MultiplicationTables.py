multiplicand = int(input('Número de la tabla de multiplicar a generar: '))
rank = range(0, 11)

for multiplier in rank:
    product = multiplicand * multiplier
    print('{} x {}\t= {}'.format(multiplicand, multiplier, product))


"""
Número de la tabla de multiplicar a generar: 9
9 x 0   = 0
9 x 1   = 9
9 x 2   = 18
9 x 3   = 27
9 x 4   = 36
9 x 5   = 45
9 x 6   = 54
9 x 7   = 63
9 x 8   = 72
9 x 9   = 81
9 x 10  = 90
"""