import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, s):
        self.site = s

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
