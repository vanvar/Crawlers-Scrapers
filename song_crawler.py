import requests
from lxml import html
import os
import time
from bs4 import BeautifulSoup
from unidecode import unidecode
import subprocess

base_url = 'http://www.tunefind.com/show'
y_url = 'https://www.googleapis.com/youtube/v3/search'

class HashSpider:

	def __init__(self, base_url):
		self.base_url = base_url
		self.songs = []

	def getShow(self):
		show = raw_input('Show : ')
		s = '-'.join(show.split())
		self.base_url += '/' + s
		return self.base_url

	def getSeason(self):
		try:
			season = int(raw_input('Season : '))
		except ValueError:
			print 'Oops! Not a valid season number. Try again...'
			getSeason()
		self.base_url += '/season-' + str(season)
		return self.base_url

	def getEpisode(self):
		try:
			episode = int(raw_input('Episode : '))
		except ValueError:
			print 'Oops! Not a valid episode number. Try again...'
			getEpisode()
		return episode

	def getSongs(self):
		self.getShow()
		self.getSeason()
		episode = self.getEpisode()
		r = requests.get(self.base_url)
		if r.status_code is 200:
			print r.url
			tree = html.fromstring(r.text)
			episode_name = tree.xpath('//ul[@class="MainList__container___3OWyj"]/li[@class="MainList__item___fZ13_"]/div/h3/a/text()')[episode-1]
			episode_link = tree.xpath('//ul[@class="MainList__container___3OWyj"]/li[@class="MainList__item___fZ13_"]/div/h3/a/@href')[episode-1]
			songs_url = 'http://www.tunefind.com' + episode_link
			print episode_name
			print songs_url
			time.sleep(2)
			f = requests.get(songs_url)
			data = f.text
			soup = BeautifulSoup(unidecode(data), 'lxml')
			for song in soup.find_all('a'):
				if song.get('title') is not None:
					self.songs.append(song.string)
			print '\n'
			return list(set(self.songs))
		else:
			print 'Error getting request from '+r.url

	def youtubeSearch(self):
		songs = self.getSongs()
		song_name = songs[0]
		payload = {'part':'snippet', 'q':song_name, 'type':'video'}
		r = requests.get(y_url, params = payload)
		data = r.json()
		print data.items()
		
spider = HashSpider(base_url)
spider.getSongs()


