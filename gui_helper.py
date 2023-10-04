from tkinter import *

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

def __rgb_to_html(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
