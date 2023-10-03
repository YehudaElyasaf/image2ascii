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

root.geometry(f'{width}x{height}+{margin_left}+{margin_top}')
root.title = 'image2ascii'
root.resizable(False, False)
icon = Image.open('./img/icon.ico')
root.iconphoto(False, ImageTk.PhotoImage(icon))

#main frame
main_frame = Frame(root, bg='#FFFFAA')
main_frame.pack(fill=BOTH, expand=True)

btn_select = Button(main_frame, text='select image', command=lambda: event_handlers.open_image(result_textbox, buttons_frame))
btn_select.pack()

#result_textbox
result_textbox = Text(main_frame, bg='#333')
result_textbox.pack(fill=BOTH, expand=True)
result_textbox['state']=DISABLED

#buttons_frame
buttons_frame = Frame(main_frame)
buttons_frame.pack(fill=BOTH)

copy_btn = Button(buttons_frame, text='copy')
copy_btn.pack(side=RIGHT, fill=X, expand=True)

convert_new_btn = Button(buttons_frame, text='convert new image')
convert_new_btn.pack(side=RIGHT, fill=X, expand=True)

disable_frame(buttons_frame)

#run
root.mainloop()
