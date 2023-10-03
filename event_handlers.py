import os
from tkinter import *
from tkinter import filedialog

from Img2Ascii import *

#globals
img2ascii = None

def open_image(result_textbox, options_frame, btn_select_image, selected_image_lbl):
    image_path = filedialog.askopenfilename(title="Select image", filetypes=(
        ('Image Files', ('*.png', '*.jpg', '*.jpeg')),
        ))
    
    if image_path == '' or image_path == ():
        #no image was selected
        return
    
    #enable butotns frame
    enable_frame(options_frame)
    
    #show image
    global img2ascii
    img2ascii = Img2Ascii(image_path)
    __show_image(result_textbox)
    
    #show selected image name in GUI
    btn_select_image['text'] = 'convert new image'
    image_filename = os.path.basename(image_path)
    selected_image_lbl['text'] = image_filename

def __show_image(result_textbox):
    global img2ascii
    ascii_mat = img2ascii.to_ascii_matrix(rows=25, is_colorful=True, invert_ascii=False)

    result_textbox['state'] = NORMAL
    result_textbox.delete('1.0', END)
    #show image
    for row in ascii_mat:
        for cell in row:
            #set color
            color = __rgb_to_hrml(cell.r, cell.g, cell.g)
            result_textbox.tag_config(color, foreground=color)
            #print letter
            result_textbox.insert(END, cell.char, color)
        
        result_textbox.insert(END, '\n')
    
    result_textbox['state'] = DISABLED

#helper methods
def __rgb_to_hrml(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def disable_frame(frame):
    for child in frame.winfo_children():
        child['state'] = DISABLED
        
def enable_frame(frame):
    for child in frame.winfo_children():
        child['state'] = ACTIVE