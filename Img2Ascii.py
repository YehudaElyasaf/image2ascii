from PIL import Image, ImageStat

from AsciiCell import *

#ration between row height to character width
CHAR_HEIGHT_WIDTH_RATIO = 2.35
MIN_ROWS = 5
MAX_ROWS = 100

class Img2Ascii:
    def __init__(self, image_path):
        self.image_path = image_path
        try:
            image = Image.open(image_path)
        except IOError:
            raise Exception(f'{image_path} is not a valid image file')
    
        #TODO: check if image has alpha channel (not supported currently)

    def __get_image_color(self, image, is_colorful, is_inverted):
        image = image.convert('RGB')
        
        if not is_colorful:
            #black color
            return 0, 0, 0

        total_r = 0
        total_g = 0
        total_b = 0

        total_pixels = image.width * image.height

        for x in range(image.width):
            for y in range(image.height):
                pixel = image.getpixel((x, y))
                if type(pixel) == int:
                    #one color
                    total_r += pixel
                    total_g += pixel
                    total_b += pixel
                else:
                    #multicolor
                    total_r += pixel[0]
                    total_g += pixel[1]
                    total_b += pixel[2]
        r, g, b = total_r // total_pixels, total_g // total_pixels, total_b // total_pixels

        if is_inverted:
            r = 255 - r
            g = 255 - g
            b = 255 - b            
        
        return r, g, b

    def __get_image_char(self, image, chars):
        brightness = ImageStat.Stat(image).rms[0]

        char_index = int((brightness / 255) * len(chars))
        if char_index < 0:
            char_index = 0
        if char_index > len(chars) - 1:
            char_index = len(chars) - 1

        return chars[char_index]
    
    def __get_cell(self, cropped_image, chars, is_colorful, invert_colors):
        r, g, b = self.__get_image_color(cropped_image, is_colorful, invert_colors)
        char = self.__get_image_char(cropped_image, chars)
        
        return AsciiCell(char, r, g, b)

    def __get_all_characters(self, invert_ascii):
        #TODO: allow user select characters (in both GUI and CLI)
        chars = '@0QO%#&o=*+~-:,. '

        if invert_ascii:
            chars = chars[::-1]
        
        return chars

    def to_ascii_matrix(self, options, rows):
        if options.invert_colors and not options.is_colorful:
            raise Exception("Can't invert colors of colorless image")

        if(rows < MIN_ROWS):
            raise Exception(f'Minimum rows allowed is {MIN_ROWS}')
        if(rows > MAX_ROWS):
            raise Exception(f'Maximum rows allowed is {MAX_ROWS}')

        chars = self.__get_all_characters(options.invert_ascii)

        image = Image.open(self.image_path)
        image.convert('RGB')
            
        pixel_height = image.height / rows
        cols = int((image.width / pixel_height) * CHAR_HEIGHT_WIDTH_RATIO)
        pixel_width = image.width / cols

        image_mat = []
        
        #TODO: sometome, image is too bright or it doesn't have enough brightness differences between pixels.
        for row in range(rows):
            row_to_add = []

            for col in range(cols):
                top = pixel_height * row
                left = pixel_width * col
                height = top + pixel_height
                width = left + pixel_width
                cropped_image = image.crop((left, top, width, height))
                cell = self.__get_cell(cropped_image, chars, options.is_colorful, options.invert_colors)

                row_to_add.append(cell)
            
            image_mat.append(row_to_add)
            
        return image_mat
