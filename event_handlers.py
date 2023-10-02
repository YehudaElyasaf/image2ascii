from tkinter import *
from tkinter import filedialog

from Img2Ascii import *

image_path = ''

def open_image(frame, properties_frame):
    global image_path
    image_path = filedialog.askopenfilename(title="Select image", filetypes=(
        ('Image Files', ('*.png', '*.jpg', '*.jpeg')),
        ))
    properties_frame.pack(fill=BOTH, expand=True)

def convert_image(main_frame, result_frame, result_textbox):
    img2ascii = Img2Ascii(image_path)
    ascii_mat = img2ascii.to_ascii_matrix(rows=25, is_colorful=True, invert_ascii=False)

    main_frame.destroy()
    result_frame.pack(fill=BOTH, expand=True)
    result_textbox.delete(END)
    #show image
    for row in ascii_mat:
        for cell in row:
            #set color
            color = rgb_to_hrml(cell.r, cell.g, cell.g)
            result_textbox.tag_config(color, foreground=color)
            #print letter
            result_textbox.insert(END, cell.char, color)
        
        result_textbox.insert(END, '\n')

    result_textbox.config(state=DISABLED)


def rgb_to_hrml(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
