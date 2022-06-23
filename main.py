import argparse

import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Crawl all the links in the Index Of website.')
parser.add_argument('--url', type=str, help='The website to be crawled.')
parser.add_argument('--parentNode', type=str, default='pre', help='parent node. Default: pre')
parser.add_argument('--parentStartPosition', type=int, default=0,
                    help="""The parent node starts grabbing the position. Default: 0""")
parser.add_argument('--childStartPosition', type=int, default=1,
                    help="""The child node starts grabbing the position. Default: 1""")
parser.add_argument('--type', type=str, default='all', help='output url type. type:all|dir|file Default: all')

args = parser.parse_args()


def getLink(url: str, parentNode: str = 'pre', parentStartPosition: int = 0, childStartPosition: int = 1):
    # print(url)
    res = requests.get(url)
    # print(res.text)
    if res.status_code == 200 and res.headers['Content-Type'].find('text/html') != -1:
        soup = BeautifulSoup(res.text, "html.parser")
        for link in soup.find_all(parentNode)[parentStartPosition].find_all("a")[childStartPosition:]:
            href = link['href']
            # 判断需要输出的类型
            if args.type == 'all':
                print(url + href)
            if args.type != 'all' and args.type == 'dir' and href[-1] == "/":
                print(url + href)
            if args.type != 'all' and args.type == 'file' and href[-1] != "/":
                print(url + href)

            if href[-1] == "/":
                getLink(url + href, parentNode, parentStartPosition, childStartPosition)
    pass


if args.url is None:
    parser.print_help()
else:
    getLink(args.url, args.parentNode, args.parentStartPosition, args.childStartPosition)
