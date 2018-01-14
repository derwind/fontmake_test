#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re
import argparse
from fontTools.ttLib import TTFont

class FamilyNameRenamer(object):
    def __init__(self, in_font, out_font, family_name):
        self.in_font = in_font
        self.out_font = out_font
        self.family_name = family_name
        self.original_family = None

    def run(self):
        font = TTFont(self.in_font)
        names = font["name"].names
        self.detect_family_name(names)
        for name in names:
            encoding = name.getEncoding()
            decoded_string = name.string.decode(encoding)
            if name.nameID == 1 or name.nameID == 4 or name.nameID == 16:
                name.string = decoded_string.replace(self.original_family, self.family_name).encode(encoding)
            elif name.nameID == 6:
                trimmed_original_family = re.sub(r"\s+", "", self.original_family)
                trimmed_family_name = re.sub(r"\s+", "", self.family_name)
                name.string = decoded_string.replace(trimmed_original_family, trimmed_family_name).encode(encoding)

        font.save(self.out_font)

    def detect_family_name(self, names):
        for name in names:
            encoding = name.getEncoding()
            decoded_string = name.string.decode(encoding)
            if name.nameID == 16:
                if self.original_family is None:
                    self.original_family = decoded_string
                    break
        if self.original_family is not None:
            return
        for name in names:
            encoding = name.getEncoding()
            decoded_string = name.string.decode(encoding)
            if name.nameID == 1:
                if self.original_family is None:
                    self.original_family = decoded_string
                    break

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("in_font", metavar="FONT", type=str,
                        help="input font")
    parser.add_argument("-o", "--output", dest="out_font", default=None,
                        help="output font")
    parser.add_argument("-f", "--family", dest="family_name", required=True,
                        help="family name")

    args = parser.parse_args()

    if args.out_font is None:
        args.out_font = args.in_font

    return args

def main():
     args = get_args()
     tool = FamilyNameRenamer(args.in_font, args.out_font, args.family_name)
     sys.exit(tool.run())

if __name__ == "__main__":
    main()
