import urllib2
f = open('out.txt', 'r')
names = map(str.strip, f)
urls = ["https://pypi.python.org/pypi/" + str(x) for x in names]


def getsource(url):
    open = urllib2.urlopen(url)
    page_source = open.read()
    return page_source


for url in urls:
    print getsource(url)
