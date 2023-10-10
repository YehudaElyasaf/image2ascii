from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import event_handlers
import config
import gui_helper
from ImgOptions import *

#GUI
root = Tk()

#root
height = 600
width = 1000

margin_left = int((root.winfo_screenwidth() - width) / 2)
margin_top = int((root.winfo_screenheight() - height) / 2)

#TODO: GUI changes: colors and buttons
root.geometry(f'{width}x{height}+{margin_left}+{margin_top}')
root.title = 'image2ascii'
root.resizable(False, False)
icon = Image.open('./img/icon.ico')
root.iconphoto(False, ImageTk.PhotoImage(icon))
root['bg'] = '#FFFF00'

#select image frame
select_image_frame = Frame(root, bg='')
select_image_frame.pack()

select_image_btn = Button(select_image_frame, text='convert image', command=lambda: event_handlers.open_image(result_textbox, options_frame, select_image_btn, selected_image_lbl, options))
select_image_btn.pack(side=LEFT, anchor=CENTER, padx=10)

selected_image_lbl = Label(select_image_frame, bg=root['bg'], fg='black', text='No image selected')
selected_image_lbl.pack(side=RIGHT, anchor=CENTER)

#result_textbox
#TODO: set font size according to rows
#TODO: allow user set forecolor (in one-color mode) and bgcolor
#TODO: save ASCII to image?
result_textbox = Text(root, bg='#fff', font=('Monospace', 10, 'bold'))
result_textbox.pack(fill=BOTH, expand=True)
result_textbox['state']=DISABLED

#options_frame
options = ImgOptions() #reads options from file

options_frame = Frame(root)
options_frame.pack(fill=X)

copy_btn = Button(options_frame, text='copy',
                          command=lambda: event_handlers.copy(result_textbox))
copy_btn.pack(side=LEFT, fill=X, expand=True)

invert_ascii_btn = Button(options_frame, text='invert ASCII',
                          command=lambda: event_handlers.invert_ascii(invert_ascii_btn, options))
invert_ascii_btn.pack(side=LEFT, fill=X, expand=True)

is_colorful_btn = Button(options_frame, text='is colorful',
                         command=lambda: event_handlers.is_colorful(is_colorful_btn, options, invert_colors_btn))
is_colorful_btn.pack(side=LEFT, fill=X, expand=True)

invert_colors_btn = Button(options_frame, text='invert colors',
                           command=lambda: event_handlers.invert_colors(invert_colors_btn, options))
invert_colors_btn.pack(side=LEFT, fill=X, expand=True)

#ADDING OPTION: (not all stages are necessarily required)
# 0. add option to ImgOptions class
# 1. add widghet here
# 2. add widget to options
# 3. add widget to method 'load_options' in gui_helper.py
# 4. add option to ImgOptions's c'tor in cli_app.py

#show options from file on GUI
#TODO: why do changes appear only on hovering?
gui_helper.show_options(options, invert_ascii_btn, is_colorful_btn, invert_colors_btn)
gui_helper.disable_frame(options_frame)

#exception handling
def report_callback_exception(self, exception, *args):
    if config.DEBUG_MODE:
        raise exception
    else:
        message = exception.args[0]
        messagebox.showerror('Error', message)
    
root.report_callback_exception = report_callback_exception

#main
if __name__ == '__main__':
    #run
    root.mainloop()
