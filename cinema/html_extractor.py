#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import urllib2 

from HTMLParser import HTMLParser  


# http://stackoverflow.com/questions/3276040/how-can-i-use-the-python-htmlparser-library-to-extract-data-from-a-specific-div

class MovieBase:
	def __init__(self):
		self.title = ''
		self.duration = -1
		self.hours = None
			
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.idDiv = 0
		self.idDivFicheFilm = 0
		self.idColToDay = 0
		self.idColToDayForAll = -1
		self.lastHour = ''
		
		self.wrap_fiche_film = False
		self.wrap_fiche_film_a = False
		self.horaires_duree = False
		self.horaires_duree_strong = False
		self.thead = False
		self.thead_th = False
		self.tbody = False
		self.tbody_td = False
		self.tbody_td_a = False
		
		self.title = ''
		self.duration = -1
		self.hours = []
		#self.day = 0
		
		self.movie = None
		self.movieList = []
		
	def handle_starttag(self, tag, attrs):
		if tag == 'div':
			self.idDiv += 1
			for name, value in attrs:
				if name == 'class' and value == 'wrap-fiche-film':
					self.idDivFicheFilm = self.idDiv -1
					self.wrap_fiche_film = True
					self.movie = MovieBase()
					break
		
		elif self.wrap_fiche_film:			
			if tag == 'a':
				# horaires
				if self.tbody_td:
					self.tbody_td_a = True
					
				# titre
				elif self.title == '':
					self.wrap_fiche_film_a = True
					
			# durée
			elif tag == 'span':		
				for name, value in attrs:
					if name == 'class' and value == 'horaires-duree':
						self.horaires_duree = True
						break
			elif tag == 'strong':
				if self.horaires_duree:
					self.horaires_duree_strong = True
			
			# jour
			elif tag == 'thead':
				self.thead = True
			elif tag == 'th':
				if self.thead:
					self.thead_th = True
					
			# horaires
			elif tag == 'tbody':
				self.tbody = True
				self.hours = []
			elif tag == 'td':
				if self.tbody:
					if self.tbody_td:
						self.hours.append(self.lastHour)
						self.lastHour = ''
					self.tbody_td = True
					self.lastHour = ''

					
	def handle_endtag(self, tag):
		if tag == 'div' and self.idDiv:
			self.idDiv -= 1
			if self.idDiv == self.idDivFicheFilm:
				if self.wrap_fiche_film:
					self.wrap_fiche_film = False
					self.movieList.append( self.movie )
					self.movie = None
					self.title = ''
					#print 'JOUR', self.idColToDayForAll
					#print ''

		elif tag == 'a':
			# horaires
			if self.tbody_td_a:
				self.tbody_td_a = False
			
			# titre
			elif self.wrap_fiche_film_a and self.title != '':
				self.wrap_fiche_film_a = False
				
		# durée
		elif tag == 'strong' and self.horaires_duree_strong:
			self.horaires_duree_strong = False
		elif tag == 'span' and self.horaires_duree:
			self.horaires_duree = False
			
		# jour
		elif tag == 'thead' and self.thead:
			self.thead = False
		elif tag == 'th' and self.thead_th:
			self.thead_th = False
			
		# horaires
		elif tag == 'tbody' and self.tbody:
			self.tbody = False
			if self.tbody_td:
				self.hours.append(self.lastHour)
				self.lastHour = ''
			#print 'HORAIRES', self.hours, self.idColToDayForAll
			#self.movie.hours = self.hours
			self.movie.hours = self.hours[self.idColToDayForAll]
			self.tbody_td = False		


	def handle_data(self, data):
		if self.wrap_fiche_film:
			# titre
			if self.wrap_fiche_film_a:
				self.title = data.replace('\t','')
				#print 'TITRE', self.title
				self.movie.title = self.title
				
			# durée
			elif self.horaires_duree_strong:
				self.duration = data
				#print 'DUREE', self.duration
				self.movie.duration = self.duration
				
			# jour
			elif self.thead_th:
				if self.idColToDayForAll < 0:
					if data == "Aujourd'hui":
						self.idColToDayForAll = self.idColToDay
					else:
						self.idColToDay += 1
						
			# horaires
			elif self.tbody_td_a:
				self.lastHour = data
				

			

import htmllib

def unescape(s):
	p = htmllib.HTMLParser(None)
	p.save_bgn()
	p.feed(s)
	return p.save_end()
	
htmlcodes = ['&Aacute;', '&aacute;', '&Agrave;', '&Acirc;', '&agrave;', '&Acirc;', '&acirc;', '&Auml;', '&auml;', '&Atilde;', '&atilde;', '&Aring;', '&aring;', '&Aelig;', '&aelig;', '&Ccedil;', '&ccedil;', '&Eth;', '&eth;', '&Eacute;', '&eacute;', '&Egrave;', '&egrave;', '&Ecirc;', '&ecirc;', '&Euml;', '&euml;', '&Iacute;', '&iacute;', '&Igrave;', '&igrave;', '&Icirc;', '&icirc;', '&Iuml;', '&iuml;', '&Ntilde;', '&ntilde;', '&Oacute;', '&oacute;', '&Ograve;', '&ograve;', '&Ocirc;', '&ocirc;', '&Ouml;', '&ouml;', '&Otilde;', '&otilde;', '&Oslash;', '&oslash;', '&szlig;', '&Thorn;', '&thorn;', '&Uacute;', '&uacute;', '&Ugrave;', '&ugrave;', '&Ucirc;', '&ucirc;', '&Uuml;', '&uuml;', '&Yacute;', '&yacute;', '&yuml;', '&copy;', '&reg;', '&trade;', '&euro;', '&cent;', '&pound;', '&lsquo;', '&rsquo;', '&ldquo;', '&rdquo;', '&laquo;', '&raquo;', '&mdash;', '&ndash;', '&deg;', '&plusmn;', '&frac14;', '&frac12;', '&frac34;', '&times;', '&divide;', '&alpha;', '&beta;', '&infin']
#newcode = ['\xc1','\xe1','\xc0','\xc2','\xe0','\xc2','\xe2','\xc4','\xe4','\xc3','\xe3','\xc5','\xe5','\xc6','\xe6','\xc7','\xe7','\xd0','\xf0','\xc9','\xe9','\xc8','\xe8','\xca','\xea','\xcb','\xeb','\xcd','\xed','\xcc','\xec','\xce','\xee','\xcf','\xef','\xd1','\xf1','\xd3','\xf3','\xd2','\xf2','\xd4','\xf4','\xd6','\xf6','\xd5','\xf5','\xd8','\xf8','\xdf','\xde','\xfe','\xda','\xfa','\xd9','\xf9','\xdb','\xfb','\xdc','\xfc','\xdd','\xfd','\xff','\xa9','\xae','\u2122','\u20ac','\xa2','\xa3','\u2018','\u2019','\u201c','\u201d','\xab','\xbb','\u2014','\u2013','\xb0','\xb1','\xbc','\xbd','\xbe','\xd7','\xf7','\u03b1','\u03b2','\u221e']
newcode = []

for index in range(len(htmlcodes)):
	newcode.append(HTMLParser.unescape.__func__(HTMLParser, htmlcodes[index]))


	


'''
p = MyHTMLParser()
f = urllib2.urlopen('http://lechaplinstlambert.cotecine.fr/horaires/')
html = f.read()

html = html.decode("iso8859-1")
for htmlcode in htmlcodes:
	if htmlcode in html:
		index = htmlcodes.index(htmlcode)
		html = html.replace( htmlcode, newcode[index] )

#print html
p.feed(html)
#print p.data
for movie in p.movieList:
	print movie.title, movie.duration, '"'+movie.hours+'"'
p.close()
'''




import datetime, threading, time

def foo():
	next_call = time.time()
	while True:
		#print datetime.datetime.now()
		# ---------------------------------------------------
		
		SMS_text = ''

		hour = str(time.localtime().tm_hour)
		min = str(time.localtime().tm_min)
		#print hour + 'h' + min
		print datetime.datetime.now()
		
		if (hour == '17' and min == '50'):
			p = MyHTMLParser()
			f = urllib2.urlopen('http://lechaplinstlambert.cotecine.fr/horaires/')
			html = f.read()

			html = html.decode("iso8859-1")
			for htmlcode in htmlcodes:
				if htmlcode in html:
					index = htmlcodes.index(htmlcode)
					html = html.replace( htmlcode, newcode[index] )

			p.feed(html)
			for movie in p.movieList:
				#print movie.title, movie.duration, '['+movie.hours+']'
				
				isValide = False
				if len(movie.hours) > 0:
					if int(movie.hours.split('h')[0]) >= 19:
						isValide = True

				if isValide:
					print movie.title + '\t' + movie.duration + '\t' + movie.hours
					if len(SMS_text) > 0: SMS_text += '\r\r'
					SMS_text += (movie.title + '\r' + movie.duration + ' - ' + movie.hours)

			p.close()
			p = None
			
			
			if len(SMS_text) > 0:
				SMS_url = 'https://smsapi.free-mobile.fr/sendmsg?user=XXXXXXXXXX&pass=KKKKKKKKKKKK&msg=helloGirls'
				SMS_url += SMS_text.replace(' ','%20').replace('\r','%0d')
				response = urllib2.urlopen(SMS_url)
		
		# ---------------------------------------------------
		next_call = next_call + 60
		time.sleep(next_call - time.time())

timerThread = threading.Thread(target=foo)
timerThread.start()

# However your application will not exit normally, you'll need to kill the timer thread. If you want to exit normally when your application is done, without manually killing the thread, you should use

'''
timerThread = threading.Thread(target=foo)
#timerThread.daemon = True
timerThread.start()
'''