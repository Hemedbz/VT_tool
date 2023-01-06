import requests


class VTAnalyzer:

    def __init__(self):
        self._cache = {}
        self._api_key = open("vt_api.txt").read()

    def _check_reputation_for_single_url(self, url :str):
        # last_analysis_date

        pass

    def get_urls_reputation(self, urls :list):
        pass
    #use multi-threading for each url
    #which means- locks
    #save the result to avoid waisted calls to api -> caching

    def scan_single_url(self, url) -> bool: #200/400
        pass




# curl --request POST \
#   --url https://www.virustotal.com/api/v3/urls \
#   --form url=<Your URL here>
#   --header 'x-apikey: <your API key>'
#

with open ("vt_api.txt") as fh:
    api_key = fh.read()
