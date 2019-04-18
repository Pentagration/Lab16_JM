#STUDENTS: Jason Pettit, Marcus Gonzalez
#CST205-40_SP19
#Module 7 Lab 16

import urllib
import os

def htmlScrape(site,openTag,closeTag):
  """Take 3 arguments:website, opening html tag and closing html tag. 
     Creates new webpage, data.html, with provided tags.
  """
  os.chdir(setMediaPath())
  file=open("data.html","w")
  article=False
  data=urllib.urlopen(site)
  for line in data.readlines():
    if openTag in line:
      article = True
    if article:
      file.write(line)
    if closeTag in line:
      article = False
  file.close()
  
htmlScrape("https://www.ign.com/","<article","</article>")
