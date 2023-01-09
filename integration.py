from cache import Cache
from vt_analyzer import VTAnalyzer

def vt_tool_for_single_url (url: str, max_age: int, local_cache: Cache, vt_a: VTAnalyzer, scan=False):
    """
    runs through the whole flow of the tool for a single url
    :param vt_a:
    :param url: str
    :param scan: bool- by default False
    :param apikey: str
    :param max_age: maximum acceptable age, in days, for data entry
    :param local_cache: Cache class instance
    :param vt_analyzer: VTAnalyzer class instance
    :return: str, is url valid
    """

    if scan:
        vt_a.scan_url(url)
        new_info = vt_a.get_reputation_for_url(url)
        local_cache.put(url, new_info)

    else:
        from_cache = local_cache.get_info(url, max_age)

        if from_cache is None:
            new_info = vt_a.get_reputation_for_url(url)
            local_cache.put(url, new_info)

        else:
            new_info = from_cache

    return new_info
