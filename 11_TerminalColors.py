__author__ = 'Cesar'

class bcolors:
    # ANSI escape sequences.
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def main():
    print(bcolors.HEADER + "Cabecera: Inicio de configuración." + bcolors.ENDC)
    print(bcolors.OKBLUE + "Logs: Ingreso a la función." + bcolors.ENDC)
    print(bcolors.OKGREEN + "Éxito: Validación exitosa." + bcolors.ENDC)
    print(bcolors.WARNING + "Alerta: Revisar conexión de BD." + bcolors.ENDC)
    print(bcolors.FAIL + "Fallo: Error de Sintaxis." + bcolors.ENDC)
    print(bcolors.ENDC + "Texto normal.")
    bcolors.disable(bcolors)  # Limpiar todos los colores.
    print("Sin colores...")


if __name__ == '__main__':
    main()