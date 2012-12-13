#!/usr/bin/python2.7
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

f = open(name,'w')
call(['curl','-s',imgurl],stdout = f)
call(['feh','--bg-center', name])
	
