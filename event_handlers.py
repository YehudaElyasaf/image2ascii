import os
import clipboard
from tkinter import *
from tkinter import filedialog

from Img2Ascii import *
import gui_helper

#globals
img2ascii = None
result_textbox = None

#select image frame buttons
def open_image(_result_textbox, options_frame, select_image_btn, selected_image_lbl, options):
    global img2ascii, result_textbox
    result_textbox = _result_textbox
    
    image_path = filedialog.askopenfilename(title="Select image", filetypes=(
        ('Image Files', ('*.png', '*.jpg', '*.jpeg')),
        ))
    
    if image_path == '' or image_path == ():
        #no image was selected
        return
    
    #show selected image name in GUI
    select_image_btn['text'] = 'convert new image'
    image_filename = os.path.basename(image_path)
    selected_image_lbl['text'] = image_filename
    
    #enable options frame
    gui_helper.enable_frame(options_frame)
    
    #show image
    img2ascii = Img2Ascii(image_path)
    gui_helper.show_image(result_textbox, img2ascii, options)

#options frame buttons
def copy(result_textbox):
    text = result_textbox.get('1.0', END) #all text
    clipboard.copy(text)

def invert_ascii(sender, options):
    options.invert_ascii = not options.invert_ascii
    
    if options.invert_ascii:
        gui_helper.select_button(sender)
    else:
        gui_helper.unselect_button(sender)
        
    gui_helper.show_image(result_textbox, img2ascii, options)
        
def is_colorful(sender, options, invert_colors_btn):
    options.is_colorful = not options.is_colorful
    
    if options.is_colorful:
        gui_helper.select_button(sender)
        invert_colors_btn['state'] = ACTIVE
    else:
        #can't invert colors of colorless image
        gui_helper.unselect_button(invert_colors_btn)
        options.invert_colors = False
        gui_helper.unselect_button(sender)
        
        invert_colors_btn['state'] = DISABLED
        
    gui_helper.show_image(result_textbox, img2ascii, options)
        
def invert_colors(sender, options):
    options.invert_colors = not options.invert_colors
    
    if options.invert_colors:
        gui_helper.select_button(sender)
    else:
        gui_helper.unselect_button(sender)
            
    gui_helper.show_image(result_textbox, img2ascii, options)
