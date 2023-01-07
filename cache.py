import json
import datetime
from threading import Lock
import exceptions

class Cache:

    def __init__(self, file_name):
        self._file_name = file_name
        self._content = {}
        self._lock = Lock()

    def __str__(self):
        return self._content

    def _load_json(self):
        """
        loads data from json file to instance
        """
        try:
            with open(f"{self._file_name}.json", "r") as fh:
                self._lock.acquire()
                self._content = json.load(fh)
                self._lock.release()
        except:
           exceptions.NoFile()

    def put(self, url, new_information):
        """
        recieves information about url, and adds to JSON
        :param url: str
        :param new_information: dictionary with last analysis date, last analysis results
        """
        self._load_json()
        self._content[url] = new_information

        try:
            with open(f"{self._file_name}.json", "w") as fh:
                self._lock.acquire()
                json.dump(self._content, fh)
                self._lock.release()
        except:
          exceptions.FailedToSave()

    def get_info(self, url: str, maxage: int):
        """gets information about url from cache file, if the data is still valid
        :param url:str
        :param maxage: maximum acceptable data entry age, in days (default = 180)
        :return dict
        """

        self._load_json()

        # check if information in cache
        if url not in self._content:
            return None

        # check if information still valid
        if datetime.datetime.now() - datetime.datetime.fromtimestamp(self._content[url]["last analysis date"], tz=datetime.timezone.utc) >= maxage:
            self._lock.acquire()
            del self._content[url]
            try:
                with open(f"{file_name}.json", "w") as fh:
                    json.dump(self._content, fh)
                self._lock.release()
                return None
            except:
                exceptions.FailedToSave()

        #give information
        return self._content[url]