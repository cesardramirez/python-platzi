# -*- coding: utf-8 -*-

"""
Ejecutar con: 'python3 main.py'
Ejecutar con 'sudo /opt/google-cloud-sdk/bin/dev_appserver.py .' para iniciarlo de manera local.
Ejecutar 'gcloud app deploy --project platzi-python-216716' para Google Cloud SDK.

Una de las ventajas de ejecutar el proyecto con Engine en vez de Flask, es que todos los cambios que se hagan directamente en código se podrán ver reflejados en la página (sin reiniciar el server).

Para visualizar la información en BD ingresar a localhost:8000 en la sección de Datastore Viewer
El módulo Flash ejecuta código una sóla vez cuando se genera una tarjeta o flash.
"""

from flask import Flask, render_template, request, flash, redirect
from contact_model import Contact

app = Flask(__name__)
app.secret_key = 'some_secret'  # Se debe colocar una llave codificada.
app.debug = True


@app.route(r'/', methods=['GET'])  # El r indica que no va descartar ningún carácter especial.
def contact_book():  # View Functions
    contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)  # Los templates se deben definir en la carpeta 'templates'


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        contact = Contact(name=request.form.get('name'),
                          phone=request.form.get('phone'),
                          email=request.form.get('email'))

        contact.put()  # Almacena el contacto en la BD.
        flash('¡Se añadió el contacto!')

    return render_template('add_contact.html')


@app.route(r'/contacts/<uid>', methods=['GET'])  # No se llama id porque esta es una palabra reservada de python.
def contact_details(uid):
    contact = Contact.get_by_id(int(uid))  # Consulta el contacto según la key que tiene el mismo en BD.
    if not contact:
        return redirect('/', code=301)  # 301: Redirección permanente.

    return render_template('contact.html', contact=contact)


@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))
    contact.key.delete()  # Elimina el contacto según la key que tiene el mismo en BD.

    return redirect('/contacts/{}'.format(contact.key.id()))


@app.route(r'/find-to-edit', methods=['POST'])
def find_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))

    return render_template('edit_contact.html', contact=contact)


@app.route(r'/update', methods=['GET', 'POST'])
def update_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))

    if request.form:
        contact.name = request.form.get('name')
        contact.phone = request.form.get('phone')
        contact.email = request.form.get('email')
        contact.put()

        flash('¡Se actualizó el contacto!')

    return render_template('edit_contact.html', contact=contact)


if __name__ == '__main__':
    app.run()
