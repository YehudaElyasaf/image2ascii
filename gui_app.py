from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from lib.tooltip import CreateToolTip

import event_handlers
import config
import gui_helper
import colors
from img2ascii import *

#GUI
root = Tk()
#root
height = 720
width = 1080

margin_left = int((root.winfo_screenwidth() - width) / 2)
margin_top = int((root.winfo_screenheight() - height) / 2)

root.geometry(f'{width}x{height}+{margin_left}+{margin_top}')

#TODO: GUI changes: colors and buttons
root.title = 'Image2Ascii'
root.resizable(False, False)
icon = Image.open('./img/icon.ico')
root.iconphoto(False, ImageTk.PhotoImage(icon))
root['bg'] = '#FFFF00'

#select image frame
select_image_frame = Frame(root, bg='')
select_image_frame.pack()

select_image_btn = Button(select_image_frame, text='convert image', command=lambda: event_handlers.open_image(result_textbox, select_characters_txt, options_frame, select_image_btn, invert_colors_btn, selected_image_lbl, options))
select_image_btn.pack(side=LEFT, anchor=CENTER, padx=10)

selected_image_lbl = Label(select_image_frame, bg=root['bg'], fg='black', text='No image selected')
selected_image_lbl.pack(side=RIGHT, anchor=CENTER)

#result_textbox
#TODO: set font size according to rows
#TODO: allow user set forecolor (in one-color mode) and bgcolor
#TODO: save ASCII to image?
result_textbox = Text(root, bg='#111', font=('Monospace', 10, 'bold'))
result_textbox.pack(fill=BOTH, expand=True)
result_textbox['state']=DISABLED

#options_frame
options = ImgOptions() #reads options from file

options_frame = Frame(root)
options_frame.pack(fill=X)

copy_btn = Button(options_frame, text='copy',
                          command=lambda: event_handlers.copy(result_textbox))
copy_btn.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(copy_btn, 'Copy', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

invert_ascii_btn = Button(options_frame, text='invert ASCII',
                          command=lambda: event_handlers.invert_ascii(invert_ascii_btn, options))
invert_ascii_btn.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(invert_ascii_btn, 'Invert ASCII', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

is_colorful_btn = Button(options_frame, text='is colorful',
                         command=lambda: event_handlers.is_colorful(is_colorful_btn, options, invert_colors_btn))
is_colorful_btn.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(is_colorful_btn, 'Color image', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

invert_colors_btn = Button(options_frame, text='invert colors',
                           command=lambda: event_handlers.invert_colors(invert_colors_btn, options))
invert_colors_btn.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(invert_colors_btn, 'Invert colors', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

forecolor_btn = Button(options_frame, text='forecolor',
                       command=None)
forecolor_btn.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(forecolor_btn, 'Font color', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

backcolor_btn = Button(options_frame, text='backcolor',
                       command=None)
backcolor_btn.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(backcolor_btn, 'Background color', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

select_characters_txt = Entry(options_frame)
select_characters_txt.pack(side=LEFT, fill=X, expand=True)
CreateToolTip(select_characters_txt, 'Select characters', background=colors.TOOLTIP_BACKGROUND, foreground=colors.TOOLTIP_FOREGROUND)

select_characters_btn = Button(options_frame, text='OK',
                           command=lambda: event_handlers.set_characters(options, select_characters_txt))
select_characters_btn.pack(side=LEFT, fill=X, expand=False)

#show options from file on GUI
#TODO: why do changes appear only on hovering?
gui_helper.show_options(options, invert_ascii_btn, is_colorful_btn, invert_colors_btn, select_characters_txt)
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
