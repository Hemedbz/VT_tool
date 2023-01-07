import parser
from cache import Cache
from vt_analyzer import VTAnalyzer
from concurrent.futures import ThreadPoolExecutor
from integration import vt_tool_for_single_url

if __name__ == '__main__':

    # get input from user
    urls = parser.args.urls.split(",")
    scan = parser.args.scan
    apikey = parser.args.apikey
    maxage = parser.args.maxage

    # create instances
    local_cache = Cache("vt_tool_cache")
    if apikey:
        vt_analyzer = VTAnalyzer(apikey)
    else:
        vt_analyzer = VTAnalyzer()

    # run tool - get information about urls
    with ThreadPoolExecutor as executor:
        futures = [executor.submit(vt_tool_for_single_url(url, maxage, local_cache, vt_analyzer)) for url in urls] #TODO

    # return information to user
    print(f"\n".join(futures))