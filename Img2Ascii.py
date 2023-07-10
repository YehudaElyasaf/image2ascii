from PIL import Image, ImageOps, ImageStat

#ration between row height to character width
CHAR_HEIGHT_WIDTH_RATIO = 2.35

class Img2Ascii:
    def __init__(self, image_path):
        self.image_path = image_path
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

    def __get_image_char(self, image):
        chars = '@#QOqo~,. '
        brightness = ImageStat.Stat(image).rms[0]

        char_index = int((brightness / 255) * len(chars))
        if char_index < 0:
            char_index = 0
        if char_index > len(chars) - 1:
            char_index = len(chars) - 1

        return chars[char_index]
    
    def __get_character(self, cropped_image, is_colorful):
        r, g, b = self.__get_image_color(cropped_image)
        char = self.__get_image_char(cropped_image)

        if is_colorful:
            return self.__colored(r, g, b, char)
        else:
            return char

    def to_ascii(self, rows=20, is_colorful=False, invert=False):
        image = Image.open(self.image_path)
        image.convert('RGB')

        if invert:
            image = ImageOps.invert(image)
            
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
                ascii += self.__get_character(cropped_image, is_colorful)
            ascii += '\n'
            
        return ascii

#demo
img = Img2Ascii('bibi.jpeg')
img = Img2Ascii('eye.jpg')
img = Img2Ascii('../tsiur.png')

print(img.to_ascii(rows=30, is_colorful=False, invert=True))
