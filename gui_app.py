from tkinter import *
from PIL import ImageTk, Image

import event_handlers

root = Tk()

#root
height = 600
width = 1000

margin_left = int((root.winfo_screenwidth() - width) / 2)
margin_top = int((root.winfo_screenheight() - height) / 2)

root.geometry(f'{width}x{height}+{margin_left}+{margin_top}')
root.title = 'image2ascii'
root.resizable(False, False)
icon = Image.open('./img/icon.ico')
root.iconphoto(False, ImageTk.PhotoImage(icon))

#main frame
main_frame = Frame(root, bg='#FFFFAA')
main_frame.pack(fill=BOTH, expand=True)

btn_select = Button(main_frame, text='select image', command=lambda: event_handlers.open_image(main_frame, properties_frame))
btn_select.pack()

#properties frame
properties_frame = Frame(main_frame, bg='#FFFFFF')

btn_convert = Button(properties_frame, text='convert', command=lambda: event_handlers.convert_image(main_frame, result_frame, result_textbox))
btn_convert.pack(side=BOTTOM)

#result frame
result_frame = Frame(root, bg='green')

result_textbox = Text(result_frame, bg='#fff')
result_textbox.pack(fill=BOTH, expand=True)

copy_btn = Button(result_frame, text='copy')
copy_btn.pack()
convert_new_btn = Button(result_frame, text='convert new image')
convert_new_btn.pack()

#run
root.mainloop()
