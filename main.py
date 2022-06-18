import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Crawl all the links in the Index Of website.')
parser.add_argument('--url', type=str, help='The website to be crawled.')
parser.add_argument('--parentNode', type=str, default='pre', help='parent node. Default: pre')
parser.add_argument('--startPosition', type=int, default=1, help='Start crawling the location. Default: 1')

args = parser.parse_args()


def getLink(url: str, parentNode: str = 'pre', startPosition: int = 1):
    # print(url)
    res = requests.get(url)
    # print(res.text)
    if res.status_code == 200 and res.headers['Content-Type'].find('text/html') != -1:
        soup = BeautifulSoup(res.text, "html.parser")
        for link in soup.find(parentNode).find_all("a")[startPosition:]:
            href = link['href']
            print(url + href)
            if href[-1] == "/":
                getLink(url + href, parentNode, startPosition)
    pass


if args.url is None:
    parser.print_help()
else:
    getLink(args.url, args.parentNode, args.startPosition)
