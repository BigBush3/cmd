import argparse
import sys

if len(sys.argv) == 1:
    print('no args')
    exit(0)
parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='+')
args = parser.parse_args(['arg'])

for i in args.arg:
    print(i)
