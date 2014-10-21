from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.PhantomJS()
f = open('out.txt', 'r')
content = f.readlines()
names = map(str.strip, content)
urls = ["https://pypi.python.org/pypi/" + str(x) for x in names]

"""
def getSource(name):
    url = "https://pypi.python.org/pypi/%s" % (name)
    # driver.get(url)
    # WebDriverWait(driver, 3)
    # page_source = driver.page_source
    # return page_source
    return url

for name in names:
    print getSource(name)
"""
