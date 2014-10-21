from bs4 import BeautifulSoup
import unicodedata

f = open('out.txt', 'w')

soup = BeautifulSoup(open("index.html"))
a = soup.findAll('a')
for link in a:
    print >> f, link.contents
