#Import all the necessary libraries
from tkinter import *

#Define the tkinter instance
win= Toplevel()
win.title("Rounded Button")

#Define the size of the tkinter frame
win.geometry("700x300")

#Define the working of the button

def my_command():
   button_dict={}
option= ["Kurti", "Jeans", "shirt", "chaddi"]

for i in option:
   def func(x=i):
      return entry_update(x)

   button_dict[i]=ttk.Button(win, text=i, command= func)
   button_dict[i].pack()

#Import the image using PhotoImage function
click_btn= PhotoImage(file='cloth.jpg')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(win, image=click_btn,command= my_command,borderwidth=0)
button.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)

win.mainloop()