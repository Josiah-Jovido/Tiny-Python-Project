#!/usr/bin/env python3
"""
Author : josiah_jovido <josiahjovido@gmail.com>
Date   : 2020-11-20
Purpose: Howler Exercise
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler Exercise',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out_fh = file=open(args.outfile, 'wt') if args.outfile else sys.stdout
    print(args.text.upper(), file=out_fh)

# --------------------------------------------------
if __name__ == '__main__':
    main()
