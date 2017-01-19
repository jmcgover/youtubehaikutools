#! /usr/bin/env python3

import os
import sys
from argparse import ArgumentParser
import json


# Logging
import logging
from logging import handlers
LOGGER = logging.getLogger(__name__)
SH = logging.StreamHandler()
FH = logging.handlers.RotatingFileHandler("log.log", maxBytes=5 * 1000000, backupCount = 5)
SH.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
FH.setFormatter(logging.Formatter("%(asctime)s:%(lineno)s:%(funcName)s:%(levelname)s:%(message)s"))
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(SH)
LOGGER.addHandler(FH)

DESCRIPTION="Retrieves all upvotes for the given username and saves them as a json file."
def get_arg_parser():
    parser = ArgumentParser(prog=sys.argv[0], description=DESCRIPTION)
    parser.add_argument("-i", "--info",
            help = "set console logging output to INFO")
    parser.add_argument("-d", "--debug",
            help = "set console logging output to DEBUG")
    parser.add_argument(
            metavar = "username",
            dest = "username",
            help = "retrieves all upvoted posts for the given username")
    parser.add_argument(
            metavar = "filename.json",
            default = "upvoted.json",
            dest = "filename",
            help = "JSON filename to save the upvoted posts information to")
    return parser

def save_as_json(object, filename, check = False):
    LOGGER.debug("Saving object as JSON to '%s'", filename)
    if check and os.path.isfile(filename):
        LOGGER.warning("File already exists!")
        return False
    with open(filename, 'w') as file:
        json.dump(object, file)
    return True

def open_json(filename, check = False):
    LOGGER.debug("Loading JSON as dictionary:'%s'", filename)
    if check and not os.path.isfile(filename):
        LOGGER.error("File doesn't exist!")
        return None
    with open(filename, 'r') as file:
        return json.load(file)

def get_upvoted_posts(username):
    upvoted = {}
    return upvoted

def main():
    # Parse Arguments
    parser = get_arg_parser()
    args = parser.parse_args()

    # Logging Information
    if args.info:
        SH.setLevel(logging.INFO)
    if args.debug:
        SH.setLevel(logging.DEBUG)

    # Get Upvoted Posts
    username = args.username
    upvoted = get_upvoted_posts(username)

    # Save Upvoted Posts
    filename = args.filename
    return 0

if __name__ == "__main__":
    rtn = main()
    sys.exit(rtn)
