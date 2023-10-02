import argparse
from Img2Ascii import *

parser = argparse.ArgumentParser(
    prog='Img2Ascii',
    description='Convert images to ASCII art',
)

parser.add_argument('filename')
parser.add_argument('-r', '--rows', help=f'select result rows ({MIN_ROWS} - {MAX_ROWS})')
parser.add_argument('-i', '--invert-ascii', action='store_const', const='invert_ascii', help='invert foreground and background')
parser.add_argument('-I', '--invert-colors', action='store_const', const='invert_colors', help='invert image\'s colors')
parser.add_argument('-c', '--colorful', action='store_const', const='colorful', help='create colored ascii art')

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
    image_mat = image.to_ascii_matrix(
        rows=rows,
        invert_ascii=args.invert_ascii is not None,
        invert_colors=args.invert_colors is not None,
        is_colorful=args.colorful is not None,
        )
    
    #print image
    for row in image_mat:
        for cell in row:
            print(cell, end='')

        print()

except Exception as e:
    raise e
    print('Error!')
    print(e.args[0])
    exit(1)