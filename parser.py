import argparse

parser = argparse.ArgumentParser(prog="VT Tool", description="Enter urls, separated with comma no space, to check their safety analysis in virustotal.com. \n"
                                                             "The program will return analysis results.\n"
                                                             "-s or --scan | optional | will force new analysis scan."
                                                             "-a or --apikey | should be followed by your api key."
                                                             "-m or --maxage | oprional | allows you to determine maximum valid age for analysis, in days (enter integer). Default 180",
                                 epilog="end of help")

parser.add_argument("urls")
parser.add_argument("-s", "--scan", action="store_true")
parser.add_argument("-a", "--apikey", default=None)
parser.add_argument("-m", "--maxage", default=180, type=int)

args = parser.parse_args()
