""" Función recursiva """

def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False
    
    middle = (low + high) // 2

    if numbers[middle] == number_to_find:
        return True
    elif numbers[middle] > number_to_find:
        return binary_search(numbers, number_to_find, low, middle - 1)
    else:
        return binary_search(numbers, number_to_find, middle + 1, high)

if __name__ == '__main__':
    numbers = [1, 3, 4, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    print('El número {} está en la lista.'.format('sí' if result else 'NO'))