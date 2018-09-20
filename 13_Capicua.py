def reverse_number(number):
    size_hundreds = 0  # Tamaño en cientos
    tens = 10
    
    while number >= tens:
        size_hundreds += 1
        tens *= 10
    
    digit_counter = 0
    reversed_number = 0
    
    while number != 0:
        value_digit = int(number / (10 ** size_hundreds))  # Valor entero de cada dígito del número.
        number = number % (10 ** size_hundreds)
        reversed_number += value_digit * (10 ** digit_counter)
        size_hundreds += -1
        digit_counter += 1
    
    return reversed_number
    

def is_capicua(number):
    return number == reverse_number(number)


def print_result(condition):
    print('{} es un capicúa.'.format(number)) if condition else print('{} no es un capicúa.'.format(number))


if __name__ == '__main__':
    # Capicúa: Número que se lee igual de izq a dere que dere a izq.
    number = int(input('Escribe una un número: '))
    print_result(is_capicua(number))