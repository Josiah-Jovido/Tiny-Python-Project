#!/usr/bin/env python3
"""
Author : josiah_jovido <Josiahjovido@gmail.com>
Date   : 2020-10-29
Purpose: To pick the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='To pick the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'an' if word.lower()[0] in 'aeiou' else 'a'
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
