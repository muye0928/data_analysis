##here is an example to use BeautifulSoup to scrpting some information from webistes
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

## open wiki- yeshiva
base_url = 'https://en.wikipedia.org/wiki'
his = ['/Yeshiva']
url = base_url +his[-1]
html = urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
print(soup.find('h1').get_text(), 'url:', his[-1])


#Find all sub_urls for wiki-links, randomly select a sub_urls and store it in "his". If no valid sub link is found, than pop last url in "his".
sub_urls = soup.find_all('a',href=re.compile('/wiki/.+'))
if len(sub_urls) != 0:
    his.append(random.sample(sub_urls, 1)[0]['href'])
else:
    # no valid sub link found
    his.pop()
print(his)

his = ['/wiki/Yeshiva']
base_url = 'https://en.wikipedia.org'
## try to print 20 timese
for i in range(20):
    url = base_url + his[-1]
    #     print(url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('h1').get_text(), 'url:', his[-1])

    sub_urls = soup.find_all('a', href=re.compile('\/wiki\/.+'))
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()