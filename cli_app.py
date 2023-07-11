import argparse
from Img2Ascii import *

parser = argparse.ArgumentParser(
    prog='Img2Ascii',
    description='Convert images to ASCII art',
)

parser.add_argument('filename')
parser.add_argument('-r', '--rows')
parser.add_argument('-i', '--invert', action='store_const', const='invert')
parser.add_argument('-c', '--colorful', action='store_const', const='colorful')

args = parser.parse_args()

rows = 20
if args.rows is not None:
    try:
        rows = int(args.rows)
    except ValueError:
        print('Error!')
        print(args.rows + ' is not a valid integer')
        exit(1)

try:
    image = Img2Ascii(args.filename)
    print(image.to_ascii(
        rows=rows,
        invert=args.invert is not None,
        is_colorful=args.colorful is not None,
        ))
except Exception as e:
    print('Error!')
    print(e.args[0])
    exit(1)