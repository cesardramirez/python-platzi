def peak_left(num_peak):
    for i in range(num_peak + 1):
        numbers.append(i)
        print(numbers)

def peak_right(num_peak):
    for i in range (num_peak + 1):
        numbers.pop()
        if numbers == [0]:
            print(numbers)
            break
        print(numbers)

if __name__=='__main__':
    num_peak = int(input('Ingresa el valor de la "cima": '))
    numbers = []
    peak_left(num_peak)
    peak_right(num_peak)


"""
Ingresa el valor de la "cima": 5
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4]
[0, 1, 2, 3]
[0, 1, 2]
[0, 1]
[0]
"""