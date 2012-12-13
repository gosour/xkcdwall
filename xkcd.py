import urllib2
from BeautifulSoup import BeautifulSoup
from subprocess import call
import os.path

path = '/mnt/shared/wallpapers/xkcd'

soup = BeautifulSoup(urllib2.urlopen('http://www.xkcd.com'))

imgurl = soup('div',id='comic')[0].img['src']
name = soup('div',id = 'comic')[0].img['alt']

name = path + '/ ' + name

if not os.path.isfile(name):
	f = open(name,'w')
	call(['curl',imgurl],stdout = f)
