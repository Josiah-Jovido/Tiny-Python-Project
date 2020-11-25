#!/usr/bin/env python3
"""
Author : josiah_jovido <Josiahjovido@gmail.com>
Date   : 2020-10-29
Purpose: To format the items in picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='To format the items in picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='item',
                        nargs='+',
                        help='Items we are bringing')

    
    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num_items = len(items)
    bringing = ''

    if args.sorted:
        items.sort()

    if num_items == 1:
        bringing = items[0]
    elif num_items == 2:
        bringing = f'{items[0]} and {items[1]}'
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
