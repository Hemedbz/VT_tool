import requests


class VTAnalyzer:

    def __init__(self, apikey=open("vt_api.txt").read()):
        self._api_key = apikey

    def get_reputation_for_url(self, url :str):

        #if doesn't exist, scan and check again

        #return: {"last analysis date" : last_analysis_date,
#       "last analysis results" : last_analysis_results}

        pass

    def scan_url(self, url) -> bool: #200/400
        pass




# curl --request POST \
#   --url https://www.virustotal.com/api/v3/urls \
#   --form url=<Your URL here>
#   --header 'x-apikey: <your API key>'
#