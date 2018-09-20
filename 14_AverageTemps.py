def average_temps_v2(temps):
    return sum(temps) / len(temps)

def average_temps(temps):
    sum_of_temps = 0
    
    for temp in temps:
        sum_of_temps += temp
    
    return sum_of_temps // len(temps)  # Realiza una división entera.

if __name__ == '__main__':
    temps = [21, 24, 24, 22, 20, 23, 24]

    print('La temperatura promedio es: {:.2f}'.format(average_temps_v2(temps)))