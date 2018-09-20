import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        # Parsear el contenido de la respuesta.
        soup = BeautifulSoup(response.content, 'html.parser')

        image_container = soup.find(id='comic')  # <div id='comic'>
        image_url = image_container.find('img')['src']  # <img src='...'>
        image_name = image_url.split('/')[-1]  # landscape_cropped.jpg
        print('Descargando la imagen {} ...'.format(image_name))

        # Descarga la imagen colocando la ruta y el nombre de la imagen.
        urlretrieve('https:{}'.format(image_url), image_name)  # "//imgs.xkcd.com/comics/landscape_cropped_(1).jpg"


if __name__ == '__main__':
    run()