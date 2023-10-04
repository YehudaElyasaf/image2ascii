import json

class ImgOptions:
    __OPTIONS_FILE_PATH = '.options.json'
    #dictionaty  key names
    __IS_COLORFUL_OPTION = 'is_colorful'
    __INVERT_ASCII_OPTION = 'invert_ascii'    
    __INVERT_COLORS_OPTION = 'invert_colors'    
    
    is_colorful =  False
    invert_ascii =  False
    invert_colors =  False
    
    def __init__(self):
        #read options from file
        try:
            self.__load_options()
        except Exception as e:
            #use default options
            pass
    
    def __load_options(self):
        '''Read options from file'''
        
        with open(self.__OPTIONS_FILE_PATH, 'r') as file:
            options = json.load(file)
            self.invert_colors = options[self.__INVERT_COLORS_OPTION]
            self.is_colorful = options[self.__IS_COLORFUL_OPTION]
            self.invert_ascii = options[self.__INVERT_ASCII_OPTION]
            
    def __save_options(self):
        '''Save options to file'''
        
        options_dict = {
            self.__IS_COLORFUL_OPTION: self.is_colorful,
            self.__INVERT_ASCII_OPTION: self.invert_ascii,
            self.__INVERT_COLORS_OPTION: self.invert_colors,
        }
    
        with open(self.__OPTIONS_FILE_PATH, 'w') as file:
            json.dump(options_dict, file, indent=1)
            