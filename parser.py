import argparse
#TODO: add comments, help explanations

parser = argparse.ArgumentParser(prog="VT Tool")
parser.add_argument("urls")
parser.add_argument("-s", "--scan", action="store_true")
parser.add_argument("-a", "--apikey", default=None)
parser.add_argument("-m", "--maxage", default=180, type=int)

args = parser.parse_args()
