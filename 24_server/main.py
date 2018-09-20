"""
Ejecutar con: 'python3 main.py'
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, ingenieros de software egresados de Platzi!'


if __name__ == '__main__':
    app.run()