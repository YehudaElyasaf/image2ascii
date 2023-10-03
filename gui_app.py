from tkinter import *
from PIL import ImageTk, Image

import event_handlers
from event_handlers import disable_frame

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

select_image_btn = Button(select_image_frame, text='convert image', command=lambda: event_handlers.open_image(result_textbox, options_frame, select_image_btn, selected_image_lbl))
select_image_btn.pack(side=LEFT, anchor=CENTER, padx=10)

selected_image_lbl = Label(select_image_frame, bg=root['bg'], fg='black', text='No image selected')#, command=lambda: event_handlers.)
selected_image_lbl.pack(side=RIGHT, anchor=CENTER)

#result_textbox
#TODO: allow user select font
#TODO: set font size according to rows
#TODO: allow user set forecolor (in one-color mode) and bgcolor
result_textbox = Text(root, bg='#222', font=('Monospace', 10, 'bold'))
result_textbox.pack(fill=BOTH, expand=True)
result_textbox['state']=DISABLED

#options_frame
#TODO: save options to file
options_frame = Frame(root)
options_frame.pack(fill=X)

copy_btn = Button(options_frame, text='copy')
copy_btn.pack(side=RIGHT, fill=X, expand=True)

disable_frame(options_frame)

#run
root.mainloop()
