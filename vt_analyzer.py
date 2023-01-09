import requests
import base64
import exceptions


class VTAnalyzer:

    def __init__(self, apikey):
        self._api_key = apikey
        self._header = {"accept": "application/json",
                        "content-type": "application/x-www-form-urlencoded",
                        "x-apikey": self._api_key}

    def get_analysis(self, url):
        """
        Gets analysis from api
        """

        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=self._header)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            raise exceptions.ResponseError

    def scan_url(self, url) -> bool:
        """
        Asks api to create new analysis
        """

        response = requests.post("https://www.virustotal.com/api/v3/urls", data=url, headers=self._header)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_reputation_for_url(self, url: str):
        """
        gets reputation if analysis exists, if not scans and then retrieves it
        """

        data = self.get_analysis(url)

        if data is None:
            scanned = self.scan_url(url)
            if not scanned:
                return "Unable to scan"

        data = self.get_analysis(url)


        last_analysis_date = data["data"]["attributes"]["last_analysis_date"]
        last_analysis_results = data["data"]["attributes"]["last_analysis_stats"]
        reputation = {"Last analysis date": last_analysis_date, "Last analysis results": last_analysis_results}

        return reputation
