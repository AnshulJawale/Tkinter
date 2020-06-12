from tkinter import *
from PIL import ImageTk, Image
import os

#* Navigating to the image directory
BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, 'Images')

#* Setting up the tkinter window
root = Tk()
root.title("Image Viewer")

#* Getting image image_list
img1 = ImageTk.PhotoImage(Image.open(os.path.join(IMAGE_DIR, 'aurora.jpg')))
img2 = ImageTk.PhotoImage(Image.open(os.path.join(IMAGE_DIR, 'galaxy.jpg')))
img3 = ImageTk.PhotoImage(Image.open(os.path.join(IMAGE_DIR, 'igloo.jpg')))
img4 = ImageTk.PhotoImage(Image.open(os.path.join(IMAGE_DIR, 'island.jpg')))
img5 = ImageTk.PhotoImage(Image.open(os.path.join(IMAGE_DIR, 'sunset.jpg')))
image_list = [img1, img2, img3, img4, img5]

#* Default Image
ind = 0
img_label = Label(root, image=image_list[ind])
img_label.grid(row=0, column=0, columnspan=3)

#? Functions
def next_():
    global image_list, img_label, ind, next_button
    
    ind += 1
    img_label.grid_forget()
    img_label = Label(root, image=image_list[ind])
    img_label.grid(row=0, column=0, columnspan=3)
    next_button = Button(root, text=">>", command=next_)
    next_button.grid(row=1, column=2)
    previous_button = Button(root, text="<<", command=previous)
    previous_button.grid(row=1, column=0)
    Button(root, text="Exit", padx=20, command=root.quit).grid(row=1, column=1)
    ind_label = Label(root, text=f"Image {ind + 1} of {len(image_list)}")
    ind_label.grid(row=2, column=0, columnspan=3, sticky='n')

    if ind == 4:
        next_button = Button(root, text=">>", state=DISABLED).grid(row=1, column=2)

def previous():
    global image_list, img_label, ind, previous_button

    ind -= 1
    img_label.grid_forget()
    img_label = Label(root, image=image_list[ind])
    img_label.grid(row=0, column=0, columnspan=3)
    next_button = Button(root, text=">>", command=next_)
    next_button.grid(row=1, column=2)
    previous_button = Button(root, text="<<", command=previous)
    previous_button.grid(row=1, column=0)
    Button(root, text="Exit", padx=20, command=root.quit).grid(row=1, column=1)
    ind_label = Label(root, text=f"Image {ind + 1} of {len(image_list)}")
    ind_label.grid(row=2, column=0, columnspan=3, sticky='n')

    if ind == 0:
        previous_button = Button(root, text="<<", state=DISABLED).grid(row=1, column=0)

#? Next, previous and exit buttons
next_button = Button(root, text=">>",  command=next_)
next_button.grid(row=1, column=2)
previous_button = Button(root, text="<<", command=previous, state=DISABLED)
previous_button.grid(row=1, column=0)
Button(root, text="Exit", padx=20, command=root.quit).grid(row=1, column=1)
ind_label = Label(root, text=f"Image {ind + 1} of {len(image_list)}")
ind_label.grid(row=2, column=0, columnspan=3, sticky='n')


root.mainloop()