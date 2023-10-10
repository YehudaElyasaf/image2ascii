import json

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
            
    def save_options(self):
        '''Save options to file'''
        
        options_dict = {
            self.__INVERT_ASCII_OPTION: self.invert_ascii,
            self.__IS_COLORFUL_OPTION: self.is_colorful,
            self.__INVERT_COLORS_OPTION: self.invert_colors,
            #in default characters ,don't save
            self.__CHARACTERS_OPTION: self.characters if self.characters != self.DEFAULT_CHARACTERS else ''
        }
    
        with open(self.__OPTIONS_FILE_PATH, 'w') as file:
            json.dump(options_dict, file, indent=1)
            