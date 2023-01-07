import requests
import base64

class VTAnalyzer:

    def __init__(self, apikey=open("vt_api.txt").read()):
        self._api_key = apikey
        self._header = {"accept": "application/json",
                       "content-type": "application/x-www-form-urlencoded",
                       "x-apikey": self._api_key}

    def get_analysis(self, url):
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=self._header)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            raise Exception

    def scan_url(self, url) -> bool:
        response = requests.post("https://www.virustotal.com/api/v3/urls", data=url, headers=self._header)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_reputation_for_url(self, url: str):
        data = self.get_analysis(url)

        if data is None:
            scanned = self.scan_url()
            if scanned:
                data = self.get_analysis(url)

        last_analysis_date = data["data"]["attributes"]["last_analysis_date"]
        last_analysis_results = data["data"]["attributes"]["last_analysis_stats"]

        return {"last analysis date" : last_analysis_date, "last analysis results" : last_analysis_results}