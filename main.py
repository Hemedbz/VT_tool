import parser
from vt_analyzer import VTAnalyzer
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':

    # get input from user
    urls = parser.args.urls.split(",")
    scan = parser.args.scan
    apikey = parser.args.apikey
    maxage = parser.args.maxage

    if apikey is None:
        with open("vt_api.txt", "r") as fh:
            apikey = fh.read()

    # create instance
    vt_analyzer = VTAnalyzer(apikey, maxage, scan)

    # run function - get information about urls
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(vt_analyzer.get_analysis, url) for url in urls]

    # present result nicely
    for url in urls:
        print(vt_analyzer.display_analysis(url))
