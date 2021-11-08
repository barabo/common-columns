#!/usr/bin/python
#
# Copyright (c) 2021 - Anaconda, Inc.
#
# TODO:
# - [ ] make this a click app
# - [ ] read data from stdin or from a first positional argument
# - [ ] --pivot - output common column values pivoted (default True)
# - [ ] --pretty - pretty-print the output for console reading (default false)
# - [ ] --savefiles - write to a pair of files file-common.csv and file-unique.csv
# - [ ] --show-common - only show the common columns (default False)
# - [ ] --stdout - write to stdout (default True unless --outfile is set)
# - [ ] --sort-columns - re-arrange columns with least entropy to most (default False)
# - [ ] --common-file - save common columns to a file with same extension (default unset)
# - [ ] --reverse-locf - apply locf stripping to data so locf will restore set (default false)
# - [ ] --verbose - output logging to stderr (default false)
# - [ ] --logfile - output logging to a file (default unset)

import sys

# TODO: figure out how to import the module / where to put this script / setuptools?
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

def main():
    # TODO: get data
    # TODO: apply flags
    return 0


if __name__ == "__main__":
    print("common-columns")
    sys.exit(main())
