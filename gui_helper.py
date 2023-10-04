from tkinter import *
from ImgOptions import *

__SELECTED_BUTTON_BG_COLOR = 'light blue'
__UNSELECTED_BUTTON_BG_COLOR = '#d9d9d9' #don't change. Determined by Tkinter

def select_button(button):
    button.config(bg=__SELECTED_BUTTON_BG_COLOR)
    
def unselect_button(button):
    button.config(bg=__UNSELECTED_BUTTON_BG_COLOR)

def disable_frame(frame):
    for child in frame.winfo_children():
        child['state'] = DISABLED
        
def enable_frame(frame):
    for child in frame.winfo_children():
        child['state'] = ACTIVE
        
def show_image(result_textbox, img2ascii, image_options):
    ascii_mat = img2ascii.to_ascii_matrix(image_options, rows=25)

    result_textbox['state'] = NORMAL
    result_textbox.delete('1.0', END)
    #show image
    for row in ascii_mat:
        for cell in row:
            #set color
            color = __rgb_to_html(cell.r, cell.g, cell.g)
            result_textbox.tag_config(color, foreground=color)
            #print letter
            result_textbox.insert(END, cell.char, color)
        
        result_textbox.insert(END, '\n')
    
    result_textbox['state'] = DISABLED
    
    #save options to file
    image_options.save_options()
    
def show_options(options, invert_ascii_btn, is_colorful_btn, invert_colors_btn):
    if options.invert_ascii:
        select_button(invert_ascii_btn)
        
    if options.is_colorful:
        select_button(is_colorful_btn)
    else:
        options.invert_colors = False
        
    if options.invert_colors:
        select_button(invert_colors_btn)

def __rgb_to_html(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
