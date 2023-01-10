# VT_tool
command line tool to access Virus Total API (w/Python3)

## How to use
in command line, run with python3, 
- positional arguments: urls, separated with comma, no space.
- optional: `-s` forces scanning for new analysis for URL.
- `-a`: to be followed with api key
- optional: `-m`: followed by maximum acceptable age for existing analysis, in days as int

## Modules
-  `main` is the file to use
- `parser` defines args from command line
- - `vt_analyzer` defines VTAnalyzer class, get analysis for URL
- `cache` defines the Cache class, which interacts with local json file
- `exceptions` defines all exceptions in module

## Requirements
The program runs on Python 3.10 but should be compatible to all Python 3.
the following libraries are used:

- concurrent.futures
- requests
- base64
- json
- datetime
- lock
