import os
import csv

class Contact:
    def __init__(self, name, phone, email):
        # Definir las variables como privadas.
        self.__name = name
        self.__phone = phone
        self.__email = email

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        index_found = self._found(name)
        if index_found >= 0:
            del self._contacts[index_found]
            self._save()
        else:
            self._not_found()

    def search(self, name):
        index_found = self._found(name)
        if index_found >= 0:
            self._print_contact(self._contacts[index_found])
        else:
            self._not_found()

    def update(self, name, phone, email):
        index_found = self._found(name)
        if index_found >= 0:
            self._update_contact(index_found)
            self._save()
        else:
            self._not_found()

    def _save(self):
        # csv: comma-separated values
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.get_name(), contact.get_phone(),
                                contact.get_email()))

    def _print_contact(self, contact):
        print('Nombre: {}'.format(contact.get_name()))
        print('Teléfono: {}'.format(contact.get_phone()))
        print('Correo Electrónico: {}'.format(contact.get_email()))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _found(self, name):
        # enumarate: Provee el índice y el elemento.
        for idx, contact in enumerate(self._contacts):
            if contact.get_name().lower() == name.lower():
                return idx
        else:
            return -1

    def _not_found(self):
        print('********************')
        print('¡Contacto no encontrado!')
        print('********************')

    def _update_contact(self, index_found):
        while True:
            command = str(input('''
                ¿Qué deseas actualizar?

                [n]ombre
                [t]eléfono
                [c]orreo electrónico
                [s]alir
            '''))
            if command == 'n':
                field = str(input('Nuevo Nombre: '))
                self._contacts[index_found].set_name(field)
            elif command == 't':
                field = str(input('Nuevo Teléfono: '))
                self._contacts[index_found].set_phone(field)
            elif command == 'c':
                field = str(input('Nuevo Correo Electrónico: '))
                self._contacts[index_found].set_email(field)
            elif command == 's':
                break
            else:
                print('Comando no encontrado.')


def run():

    contact_book = ContactBook()

    try:
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                # El row == [] se coloca por si al final del archivo no hay una línea vacía (salto de línea).
                if index == 0 or row == []:
                    # Salta la primera fila que tiene los nombres de los campos 'name,phone,email'.
                    continue
                contact_book.add(row[0], row[1], row[2])
    except FileNotFoundError:
        print('No existe el archivo \'contacts.csv\'. Debe añadir un nuevo contacto para crearlo.')

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)
        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto a actualizar: '))
            contact_book.update(name, phone, email)
        elif command == 'b':
            name = str(input('Escribe el nombre del contacto a buscar: '))
            contact_book.search(name)
        elif command == 'e':
            name = str(input('Escribe el nombre del contacto a eliminar: '))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    os.system('clear')
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()
