import argparse

from Img2Ascii import *
from ImgOptions import *
import config

parser = argparse.ArgumentParser(
    prog='Img2Ascii',
    description='Convert images to ASCII art',
)

parser.add_argument('filename')
parser.add_argument('-r', '--rows', help=f'select result rows ({MIN_ROWS} - {MAX_ROWS})')
parser.add_argument('-c', '--chars', help=f'select characters\nSupported characters: {Img2Ascii.SUPPORTED_CHARACTERS_ORDERED}')
parser.add_argument('-i', '--invert-ascii', action='store_const', const='invert_ascii', help='invert foreground and background')
parser.add_argument('-I', '--invert-colors', action='store_const', const='invert_colors', help='invert image\'s colors')
parser.add_argument('-C', '--colorful', action='store_const', const='colorful', help='create colored ascii art')

args = parser.parse_args()

rows = ImgOptions.DEFAULT_ROWS
if args.rows is not None:
    try:
        rows = int(args.rows)
    except ValueError:
        print('Error!')
        print(args.rows + ' is not a valid integer')
        exit(1)

characters = ImgOptions.DEFAULT_CHARACTERS
if args.chars is not None:
    characters = args.chars

try:
    image = Img2Ascii(args.filename)
    options = ImgOptions(
        invert_ascii=args.invert_ascii is not None,
        invert_colors=args.invert_colors is not None,
        is_colorful=args.colorful is not None,
        characters=characters,
    )
    image_mat = image.to_ascii_matrix(
        #TODO: move rows to ImgOptions object
        options=options,
        rows=rows,
    )
    
    #print image
    for row in image_mat:
        for cell in row:
            print(cell, end='')

        print()

except Exception as e:
    if config.DEBUG_MODE:
        raise e
    else:
        print('Error!')
        print(e.args[0])
        exit(1)
        