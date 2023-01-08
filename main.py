import datetime
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

    if apikey is None:
        with open ("vt_api.txt", "r") as fh:
            apikey = fh.read()

    # create instances
    local_cache = Cache("vt_tool_cache")
    vt_analyzer = VTAnalyzer(apikey)

    # run tool - get information about urls
    with ThreadPoolExecutor as executor:
        futures = [executor.submit(vt_tool_for_single_url(url, maxage, local_cache, vt_analyzer, scan)) for url in urls]

    #present result nicely
    printable = []
    for future in futures:
        last_analysis_date = datetime.datetime.strftime(datetime.datetime.fromtimestamp(future["Last analysis date"], tz=datetime.timezone.utc), "%Y-%m%-%d")
        last_analysis_results = future["Last analysis results"]
        presentable_string = f"Virus Total analysis for {url}:\n" \
                             f"analysis date: {last_analysis_date}\n" \
                             f"analysis results:{last_analysis_results}\n"
        printable.append(presentable_string)

    print("\n".join(printable))
