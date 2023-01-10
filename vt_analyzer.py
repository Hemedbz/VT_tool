import requests
import base64
import exceptions
from cache import Cache
import datetime

class VTAnalyzer:

    def __init__(self, apikey, max_age, to_scan=False):
        self._api_key = apikey
        self._header = {"accept": "application/json",
                        "content-type": "application/x-www-form-urlencoded",
                        "x-apikey": self._api_key}
        self._cache = Cache("vt_tool_cache")
        self._max_age = max_age
        self._scan = to_scan

    @staticmethod
    def _get_analysis_age(data):

        today = datetime.datetime.now(tz=datetime.timezone.utc)
        analysis_day = datetime.datetime.fromtimestampdatamp(data["data"]["attributes"]["last_analysis_date"],
                                                             tz=datetime.timezone.utc)
        delta = int((today - analysis_day).days)
        return delta

    def _get_analysis_from_vt(self, url):
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

    def _scan_url_in_vt(self, url) -> bool:
        """
        Asks api to create new analysis
        """

        response = requests.post("https://www.virustotal.com/api/v3/urls", data=url, headers=self._header)
        if response.status_code == 200:
            return True
        else:
            return False

    def _get_reputation_for_url_from_vt(self, url: str):
        """
        gets reputation if analysis exists, if not scans and then retrieves it
        """

        data = self._get_analysis_from_vt(url)
        analysis_age = self._get_analysis_age(data)

        if data is None or analysis_age >= self._max_age:
            scanned = self._scan_url_in_vt(url)
            if not scanned:
                return "Unable to scan"

        data = self._get_analysis_from_vt(url)

        last_analysis_date = data["data"]["attributes"]["last_analysis_date"]
        last_analysis_results = data["data"]["attributes"]["last_analysis_stats"]
        reputation = {"Last analysis date": last_analysis_date, "Last analysis results": last_analysis_results}

        return reputation

    def get_analysis(self, url):

        if not self._scan:
            information = self._cache.get_info(url, self._max_age)
            if information is None:
                information = self._get_reputation_for_url_from_vt(url)
                self._cache.put(url, information)
        elif self._scan:
            self._scan_url_in_vt(url)
            information = self._get_reputation_for_url_from_vt(url)
            self._cache.put(url, information)

        return information

    def display_analysis(self, url):
        last_analysis_date = datetime.datetime.strftime (
            datetime.datetime.fromtimestamp (
                self._cache.display_cache()[url]["Last analysis date"], tz=datetime.timezone.utc), "%Y-%m%-%d")
        last_analysis_results = self._cache.display_cache()[url]["Last analysis results"]
        presentable_string = f"Virus Total analysis for {url}:\n" \
                             f"analysis date: {last_analysis_date}\n" \
                             f"analysis results:{last_analysis_results}\n"
        return presentable_string

