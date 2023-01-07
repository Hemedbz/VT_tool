import cache
import vt_analyzer


def vt_tool_for_single_url (url: str, maxage: int, local_cache: cache.Cache, vt_a: vt_analyzer.VTAnalyzer, scan=False):
    """
    runs through the whole flow of the tool for a single url
    :param url: str
    :param scan: bool- by default False
    :param apikey: str
    :param maxage: maximum acceptable age, in days, for data entry
    :param local_cache: Cache class instance
    :param vt_analyzer: VTAnalyzer class instance
    :return: str, is url valid
    """

    if scan:
        vt_a.scan_url(url)
        new_info = vt_a.get_reputation_for_url(url)
        last_analysis_date = new_info["last_analysis_date"]
        last_analysis_results = new_info["last_analysis_results"]
        local_cache.put(url, last_analysis_date, last_analysis_results)

    else:
        from_cache = local_cache.get_info(url, maxage)

        if from_cache is None:
            new_info = vt_a.get_reputation_for_url(url)
            last_analysis_date = new_info["last_analysis_date"]
            last_analysis_results = new_info["last_analysis_results"]
            local_cache.put(url, last_analysis_date, last_analysis_results)

        else:
            new_info = local_cache.get_info(url, maxage)

    return new_info

