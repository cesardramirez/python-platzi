import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime, date, time, timedelta

def run():
	comics_amount = int(input('Cuántos días ha estado sin leer comics?\nA// '))

	today = date.today()
	
	for i in range (0, comics_amount):
		comic_day = today - timedelta(days = i)
 
		response = requests.get('http://www.gocomics.com/doonesbury/{}/{}/{}'.format(comic_day.year, comic_day.month, comic_day.day))
		soup = BeautifulSoup(response.content, 'html.parser')

		image_container = soup.find('picture', {'class':'item-comic-image'})
		image_url = image_container.find('img')['src']
        image_name = 'doonesbury-{}-{}-{}.jpg'.format(comic_day.year, comic_day.month, comic_day.day)
        print('Descargando la imagen {} ...'.format(image_name))	

		urlretrieve('{}'.format(image_url), image_name)


if __name__ == '__main__':
	run()