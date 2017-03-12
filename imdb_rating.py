from lxml import html
import requests
import json
from unidecode import unidecode

api_url = 'http://www.omdbapi.com/'
keys = ['Title', 'Year', 'imdbRating', 'Director', 'Actors', 'Genre', 'totalSeasons']

class Hash():

	def __init__(self, title, url):
		self.title = title
		self.url = url

	def jsonContent(self):
		
		payload = {'t':self.title}
		movie = requests.get(self.url, params = payload)
		return movie.json()

	def getInfo(self):
		data = self.jsonContent()
		print '\n'
		for key, value in data.items():
			if key in keys:
				print key + ' : ' + unidecode(value)

movie = raw_input('Movie/TV Show : ')
crawler = Hash(movie, api_url)
crawler.getInfo()

