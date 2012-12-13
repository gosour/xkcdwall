# A python xkcd wallpaper setter
# Uses feh
# Changes .fehbg to the latest xkcd
# Use 'eval $(cat ~/.fehbg)' in .xinitrc for change in starttup
# Else use it here for immediate action

import urllib2
from BeautifulSoup import BeautifulSoup
from subprocess import call
import os.path

user = 'sourav'
path = '/mnt/shared/wallpapers/xkcd'

soup = BeautifulSoup(urllib2.urlopen('http://www.xkcd.com'))

imgurl = soup('div',id='comic')[0].img['src']
name = soup('div',id = 'comic')[0].img['alt']

name = path + '/' + name + '.png'

if not os.path.isfile(name):
	f = open(name,'w')
	call(['curl',imgurl],stdout = f)
	feh = 'feh  --bg-center ' +  name
	f = open('/home/'+ user + '/.fehbg' , 'w')
	f.write(feh)
	
