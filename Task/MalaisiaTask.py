from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Trip to Malaysia")
window.geometry("310x100")
window.config(bg="teal")

e_amount=Entry(window)
e_amount.grid(row=2,column=2)
lbl_main=Label(window,text="Please Enter Your Amount.")
lbl_main.grid(row=1,column=2)



def check():
    amount=int(e_amount.get())
    try:
        if amount < 3000:
          raise ValueError(messagebox.showinfo('Message',"Please deposit more funds"))

    except ValueError:
        print(ValueError)
        e_amount.delete(0,END)

    else:
        (messagebox.showinfo('Message',"CONGRADULATIONS!!! YOU qualify for a trip to Malaysia"))



b_verify=Button(window,text="Check", command=check)
b_verify.grid(row=3,column=2)
window.mainloop()





