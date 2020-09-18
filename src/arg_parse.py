# arg_parse.py

import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
            description="A simple argument parser",
            epilog="This is where you might put example usage"
        )

    parser.add_argument('-arg1', '--argument1' , action="store", required=True, help='Help for option X')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-arg2', '--argument2', help='Help for option Y', default=False)
    group.add_argument('-arg3', '--argument3', help='Help for option Z', default=10)
    print(parser.parse_args())
    return parser.parse_args()

if __name__ == '__main__':
    get_args()