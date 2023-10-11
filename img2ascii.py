import json
from PIL import Image, ImageStat

#ration between row height to character width
CHAR_HEIGHT_WIDTH_RATIO = 2.35
MIN_ROWS = 5
MAX_ROWS = 150

class Img2Ascii:
    #all supported letters, sorted from biggest to smallest
    SUPPORTED_CHARACTERS_ORDERED = 'NBWM0@RD#8H69KEAQOGSPXFUZV&$gmdbqpae3542hk%CYTJIyL{}wonusxzftc17jlvi[]?/\\()<>=r+*!;:~"^,_-.\'` '
    
    def __init__(self, image_path):
        self.image_path = image_path
        
        #check if image exists
        try:
            Image.open(image_path)
        except IOError:
            raise Exception(f'{image_path} is not a valid image file')
    
        #TODO: check if image has alpha channel (not supported currently)

    def __get_image_color(self, image, is_colorful, is_inverted):
        image = image.convert('RGB')
        
        if not is_colorful:
            #white color
            return 255, 255, 255

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

    def __order_characters(self, options):
        #remove duplicate characters
        options.characters = set(options.characters)
        
        try:
            #sort
            options.characters = sorted(options.characters, key=lambda char: self.SUPPORTED_CHARACTERS_ORDERED.index(char))
            options.characters = ''.join(options.characters)
        except ValueError:
            #not supported character
            #find character
            for char in options.characters:
                if self.SUPPORTED_CHARACTERS_ORDERED.find(char) == -1:
                    raise ValueError(f"Character '{char}' is not supported.\nSupported characters: {self.SUPPORTED_CHARACTERS_ORDERED}(including whitespace)")
        
        if options.invert_ascii:
            options.characters = options.characters[::-1]

    def to_ascii_matrix(self, options, rows):
        #validate input
        if options.invert_colors and not options.is_colorful:
            raise Exception('Can\'t invert colors of colorless image')
        
        if len(options.characters) == 0:
            raise Exception('No character selected')

        if(rows < MIN_ROWS):
            raise Exception(f'Minimum rows allowed is {MIN_ROWS}')
        if(rows > MAX_ROWS):
            raise Exception(f'Maximum rows allowed is {MAX_ROWS}')
            
        self.__order_characters(options)

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
                cell = self.__get_cell(cropped_image, options.characters, options.is_colorful, options.invert_colors)

                row_to_add.append(cell)
            
            image_mat.append(row_to_add)
            
        return image_mat

class AsciiCell:
    def __init__(self, char, r, g, b):
        self.char = char
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(self.r, self.g, self.b, self.char)

#ADDING OPTION: (not all stages are necessarily required)
# 1. add option to ImgOptions class
# 2. add widget ing gui_app.py
# 3. add widget to method 'show_options' in gui_helper.py
# 4. add option to ImgOptions's c'tor in cli_app.py

class ImgOptions:
    __OPTIONS_FILE_PATH = '.options.json'
    #dictionaty key names
    __INVERT_ASCII_OPTION = 'invert_ascii'    
    __IS_COLORFUL_OPTION = 'is_colorful'
    __INVERT_COLORS_OPTION = 'invert_colors'    
    __CHARACTERS_OPTION = 'characters'
      
    #defualt values
    DEFAULT_ROWS = 25
    DEFAULT_CHARACTERS = 'YEHUDAyehuda+:<>#&. '
    
    invert_ascii = False
    is_colorful = False
    invert_colors = False
    characters = DEFAULT_CHARACTERS
    
    def __init__(self, invert_ascii=None, is_colorful=None, invert_colors=None, characters=None):
        if invert_ascii is None or is_colorful is None or invert_colors is None or characters is None:
            #read options from file
            try:
                self.__load_options()
            except Exception as e:
                #use default options
                pass
        else:
            self.invert_ascii = invert_ascii
            self.is_colorful = is_colorful
            self.invert_colors = invert_colors
            self.characters = characters
    
    def __load_options(self):
        '''Read options from file'''
        
        with open(self.__OPTIONS_FILE_PATH, 'r') as file:
            options = json.load(file)
            self.invert_ascii = options[self.__INVERT_ASCII_OPTION]
            self.is_colorful = options[self.__IS_COLORFUL_OPTION]
            self.invert_colors = options[self.__INVERT_COLORS_OPTION]
            self.characters = options[self.__CHARACTERS_OPTION]
    
    def __is_default_characters_selected(self):
        '''Check if selected characters are default characters (in any order)'''
        
        if len(self.characters) != len(self.DEFAULT_CHARACTERS):
            return False
        
        for char in self.characters:
            if self.DEFAULT_CHARACTERS.find(char) == -1:
                #character is't in default characters
                return False
        
        #all characters are in default characters
        return True
            
    def save_options(self):
        '''Save options to file'''
        
        options_dict = {
            self.__INVERT_ASCII_OPTION: self.invert_ascii,
            self.__IS_COLORFUL_OPTION: self.is_colorful,
            self.__INVERT_COLORS_OPTION: self.invert_colors,
            #in default characters ,don't save
            self.__CHARACTERS_OPTION: '' if self.__is_default_characters_selected() else self.characters
        }
    
        with open(self.__OPTIONS_FILE_PATH, 'w') as file:
            json.dump(options_dict, file, indent=1)
    