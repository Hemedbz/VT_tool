import parser
import futures.concurrent


if __name__ == '__main__':
    pass

urls = parser.args.urls.split(",")
scan = parser.args.scan
apikey = parser.args.apikey
maxage = parser.args.maxage

for url in urls:
    with open(futures.concurrent.ThreadPoolExecutor) as executor:
        pass