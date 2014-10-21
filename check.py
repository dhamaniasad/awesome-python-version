# encoding=utf8
import urllib2
import textract
import random
import string
import sys
reload(sys)
sys.setdefaultencoding('utf8')
f = open('out.txt', 'r')
names = map(str.strip, f)
urls = ["https://pypi.python.org/pypi/" + str(x) for x in names]


def getsource(url):
    open = urllib2.urlopen(url)
    page_source = open.read()
    return page_source


for url in urls:
    tempname = ''.join(random.choice(string.ascii_uppercase)
                       for i in range(10))
    tempname = tempname + ".html"
    source = getsource(url)
    file = open('/tmp/%s' % (tempname), 'w')
    file.write(source)
    file.close()
    text = textract.process('/tmp/%s' % (tempname))
    py3 = "Python :: 3"
    if py3 in text:
        return True
    else:
        return False
