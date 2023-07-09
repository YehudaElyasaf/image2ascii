from tkinter import *
from tkinter import filedialog

def open_image(frame, properties_frame):
    image_path = filedialog.askopenfilename(title="Select image", filetypes=(
        ('image files', ('*.png', '*.jpg'))))
    properties_frame.pack(fill=BOTH, expand=True)

def convert_image():
    pass