import urllib.request
import ssl
from bs4 import BeautifulSoup


class Connection:

    def __init__(self):
        https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
        opener = urllib.request.build_opener(https_sslv3_handler)
        urllib.request.install_opener(opener)

    def openpage(self, url):
        return urllib.request.urlopen(url)

    def getpage(self, url):
        with urllib.request.urlopen(url) as doc:
            return doc.read().decode('utf-8')

    def getpagehtml(self, url, parser):
        return BeautifulSoup(urllib.request.urlopen(url), parser)

