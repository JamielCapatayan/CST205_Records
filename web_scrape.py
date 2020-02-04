from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint

my_site = "https://thespaces.com/"

req = Request(
    my_site,
    headers={'User-Agent':'Moszilla/5.0'}
)

resp = urlopen(req)
bs_obj = BeautifulSoup(resp.read(), 'lxml')

title = bs_obj.body.h1
print(title.get_text())

for link in bs_obj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
