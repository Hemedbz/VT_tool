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
        if datetime.datetime.now() - self._content[url]["last analysis date"] >= maxage:
            del self._content[url]
        #TODO: how to save?
            return None

        #retrieve info
        last_analysis_date = self._content[url]["last analysis date"]
        last_analysis_results = self._content[url]["last analysis results"]
        return last_analysis_date, last_analysis_results

        with open(f"{file_name}.json", "w") as fh:
            json.dump(self._content, fh)