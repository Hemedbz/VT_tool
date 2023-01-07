# VT_tool
command line tool to access Virus Toal API (w/Python3)

## Modules
- `parser` interacts with command line
- `cache` defines the Cache class, which interacts with local json file
- `vt_analyzer` defines VTAnalyzer class, which interacts with API
- `exceptions` defines all exceptions in module
- `integration` integrates all of the above to one flow function
-  `main` is the file to use

## Requirements
The program runs on Python 3.10 but should be compatible to all Python 3.
the following libraries are used:

- concurrent.futures
- requests
- base64
- json
- datetime
- lock
