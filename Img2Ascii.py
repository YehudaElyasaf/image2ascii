from PIL import Image, ImageOps, ImageStat

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
        #TODO: check image format

    def __colored(self, r, g, b, char):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, char)

    def __get_image_color(self, image):
        total_r = 0
        total_g = 0
        total_b = 0

        total_pixels = image.width * image.height

        for x in range(image.width):
            for y in range(image.height):
                pixel = image.getpixel((x, y))
                total_r += pixel[0]
                total_g += pixel[1]
                total_b += pixel[2]
        r, g, b = total_r // total_pixels, total_g // total_pixels, total_b // total_pixels
        
        return r, g, b

    def __get_image_char(self, image, chars):
        brightness = ImageStat.Stat(image).rms[0]

        char_index = int((brightness / 255) * len(chars))
        if char_index < 0:
            char_index = 0
        if char_index > len(chars) - 1:
            char_index = len(chars) - 1

        return chars[char_index]
    
    def __get_character(self, cropped_image, is_colorful, chars):
        r, g, b = self.__get_image_color(cropped_image)
        char = self.__get_image_char(cropped_image, chars)

        if is_colorful:
            return self.__colored(r, g, b, char)
        else:
            return char

    def __get_all_characters(self, invert):
        chars = '@#QOqo~,. '

        if invert:
            chars = chars[::-1]
        
        return chars

    def to_ascii(self, rows, is_colorful=False, invert=False):
        if(rows < MIN_ROWS):
            raise Exception(f'Minimum rows allowed is {MIN_ROWS}')
        if(rows > MAX_ROWS):
            raise Exception(f'Maximum rows allowed is {MAX_ROWS}')

        chars = self.__get_all_characters(invert)

        image = Image.open(self.image_path)
        image.convert('RGB')
            
        pixel_height = image.height / rows
        cols = int((image.width / pixel_height) * CHAR_HEIGHT_WIDTH_RATIO)
        pixel_width = image.width / cols

        ascii = ''
        for row in range(rows):
            for col in range(cols):
                top = pixel_height * row
                left = pixel_width * col
                height = top + pixel_height
                width = left + pixel_width
                cropped_image = image.crop((left, top, width, height))
                ascii += self.__get_character(cropped_image, is_colorful, chars)
            ascii += '\n'
            
        return ascii

