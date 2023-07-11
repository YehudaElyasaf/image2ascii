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
    ascii_text = img2ascii.to_ascii(rows=20, is_colorful=False, invert_ascii=False)

    main_frame.destroy()
    result_frame.pack(fill=BOTH, expand=True)
    
    result_textbox.delete(END)
    result_textbox.insert(END, ascii_text)
    result_textbox.config(state=DISABLED)