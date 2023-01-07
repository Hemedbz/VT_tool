import os
import json
import datetime

#{
# url : {"last analysis date" : last_analysis_date,
#       "last analysis results" : last_analysis_results}
# }

class Cache:

    def __init__(self, file_name):
        self._content = {}
        self._file_name = file_name

    def __str__(self):
        with open(f"{self._file_name}.json", "w") as fh:
            return json.load(fh)

    def put(self, url, last_analysis_date, last_analysis_results):
        """
        recieves information about url, and adds to JSON
        :param url: str
        :param last_analysis_date: float representing UTC timestamp
        :param last_analysis_results: str
        """

        with open(f"{self._file_name}.json", "w") as fh:
            self._content = json.load(fh)
            self._content[url] = {"last analysis date": last_analysis_date, "last analysis results": last_analysis_results}
            self._content.json.dump(fh)

    def get_info(self, url: str, maxage: int):

        with open(f"{self._file_name}.json", "w") as fh:
            self._content = json.load(fh)

        #check if url in file
        if url not in self._content:
            return None

        #check if analysis expired
        if datetime.datetime.now() - datetime.datetime.fromtimestamp(self._content[url]["last analysis date"], tz=datetime.timezone.utc) >= maxage:
            del self._content[url]
        #TODO: how to save?
            return None

        #give information
        last_analysis_date = datetime.datetime(self._content[url]["last analysis date"])
        last_analysis_results = self._content[url]["last analysis results"]
        return last_analysis_date, last_analysis_results

        with open(f"{file_name}.json", "w") as fh:
            json.dump(self._content, fh)