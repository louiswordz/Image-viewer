from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer")
root.iconbitmap('logo1.jpeg')

img1 = ImageTk.PhotoImage(Image.open('product-6.png'))
img2 = ImageTk.PhotoImage(Image.open('product-10.png'))
img3 = ImageTk.PhotoImage(Image.open('product-4.png'))
img4 = ImageTk.PhotoImage(Image.open('product-11.png'))
img5 = ImageTk.PhotoImage(Image.open('chair.jpg'))

image_list = [img1, img2, img3, img4, img5]




label1 = Label(image=img1)
label1.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global label1
    global button_forward
    global button_back
    
    label1.grid_forget()
    label1 = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    
    label1.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text=f"image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)

    


def back(image_number):
    global label1
    global button_forward
    global button_back

    label1.grid_forget()
    label1 = Label(image=image_list[image_number -1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)


    label1.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text=f"image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)

    
    
button_back= Button(root, text="<<", command=back)
button_quit = Button(root, text="End Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)

status = Label(root, text=f"image {1} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky= W+E)


root.mainloop()