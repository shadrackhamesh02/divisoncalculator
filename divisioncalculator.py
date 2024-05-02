import tkinter.messagebox
from tkinter import *

obj = Tk()
obj.geometry('400x400')
obj.title('operations')
obj.configure(bg='yellow')  

# preforming operations

def div():
    num1 = int(number1.get())
    num2 = int(number2.get())
    result = num1 / num2 
    tkinter.messagebox.showinfo('Result data', 'Total: ' + str(result))

# adding labels

Label(obj, text='Enter value 1:', font=('Calibri', 20), bg='pink').place(x=10, y=30)
Label(obj, text='Enter value 2:', font=('Calibri', 20), bg='pink').place(x=10, y=80)

# declaring variables
number1 = IntVar()
number2 = IntVar()

# adding textboxes

Entry(obj, textvariable=number1, font=('Calibri', 15)).place(x=180, y=30)
Entry(obj, textvariable=number2, font=('Calibri', 15)).place(x=180, y=80)


# adding buttons

Button(obj, text='Div', font=('Calibri', 15), bg='red', fg='white', width='12', height='1', command=div).place(x=200, y =200)
obj.mainloop()