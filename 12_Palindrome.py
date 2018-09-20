""" Recorrer String """

def palindrome_v2(word):
    return True if word == word[::-1] else False

def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    return False

def print_result_v2(condition):
    print('{} {} es un palíndromo.'.format(word, 'sí' if condition else 'no'))

def print_result(condition):
    if condition:
        print('{} sí es un palíndromo.'.format(word))
    else:
        print('{} no es un palíndromo.'.format(word))


if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))
    print_result_v2(palindrome_v2(word))