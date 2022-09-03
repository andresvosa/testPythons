from tkinter import *


def my_click():
    my_label_3 = Label(root, text=myEntry.get())
    my_label_3.grid()  # Kui määrata kindel koht siis siin pannakse need
    # labelid üksteise peale


root = Tk()
# creating label
myLabel1 = Label(root, text='Hello World')  # .grid(row=0, column=0)
myLabel2 = Label(root, text='My name is Andres')  # .grid(row=1, column=0)
myButton1 = Button(root, text='Enter text', padx=50, pady=20, command=my_click, fg='red',
                   bg='blue')  # , state= DISABLED
myEntry = Entry(root, width=50)
# showing label 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton1.grid(row=2, column=0)
myEntry.grid(row=2, column=1)
# Empty columns doesn't affect layout
# run mainloop
root.mainloop()
