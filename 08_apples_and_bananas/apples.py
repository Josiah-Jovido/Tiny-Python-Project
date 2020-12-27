#!/usr/bin/env python3
"""
Author : josiah-jovido <josiahjovido@gmail.com>
Date   : 2020-12-27
Purpose: Apples and Bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel',
                        metavar='str',
                        type=str,
                        choices='aeiou',
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    
    for v in 'aeiou':
        text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    print(text)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
