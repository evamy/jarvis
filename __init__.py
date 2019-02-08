#!/Users/evamy/bot/bin/python
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# from . import *
import argparse
from server.respond import getResponse


parser = argparse.ArgumentParser(description="Extract intent from statement")
parser.add_argument("-c", "--command", type=str,
                    help="write a command for a response")

args = parser.parse_args()

getResponse(args.command)
