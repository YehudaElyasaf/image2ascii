from tkinter import *
from PIL import ImageTk, Image
import os

import event_handlers

root = Tk()

#root
height = 600
width = 1000

margin_left = int((root.winfo_screenwidth() - width) / 2)
margin_top = int((root.winfo_screenheight() - height) / 2)

root.geometry(f'{width}x{height}+{margin_left}+{margin_top}')
root.title = 'image2ascii'

#main frame
main_frame = Frame(root, bg='#FFFFAA')
main_frame.pack(fill=BOTH, expand=True)
btn_select = Button(main_frame, text='select image', command=lambda: event_handlers.open_image(main_frame, properties_frame))
btn_select.pack()

#properties frame
properties_frame = Frame(main_frame, bg='#FFFFFF')
btn_convert = Button(properties_frame, text='convert', command=lambda: event_handlers.convert_image())
btn_convert.pack(side=BOTTOM)

#run
root.mainloop()
