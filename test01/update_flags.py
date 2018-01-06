#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re
import argparse
from fontTools.ttLib import TTFont

class FlagsUpdater(object):
    def __init__(self, in_font, out_font):
        self.in_font = in_font
        self.out_font = out_font

    def run(self):
        font = TTFont(self.in_font)
        font["head"].flags |= 0x1 << 1
        font.save(self.out_font)

        return 0

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("in_font", metavar="FONT", type=str,
                        help="input font")
    parser.add_argument("-o", "--output", dest="out_font", default=None,
                        help="output font")

    args = parser.parse_args()

    if args.out_font is None:
        args.out_font = args.in_font

    return args

def main():
     args = get_args()
     tool = FlagsUpdater(args.in_font, args.out_font)
     sys.exit(tool.run())

if __name__ == "__main__":
    main()
