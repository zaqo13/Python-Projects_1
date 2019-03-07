from tkinter import *

window=Tk()
def kg():
    print(e1_val.get())
    gm=float(e1_val.get())*1000
    pounds=float(e1_val.get())*2.20462
    ounce=float(e1_val.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END,gm)
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    t3.delete("1.0",END)
    t3.insert(END,ounce)

b1=Button(window,text="Convert",command=kg)
b1.grid(row=0,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)
e2=Label(window,text="Kg")
e2.grid(row=0,column=2)

# t1_val=StringVar()    #we ccan ot give StringVar() to Text widget, it only be given to Entry widget
t1=Text(window,height=1,width=15)
t1.grid(row=0,column=3)
t4=Label(window,text="grams")
t4.grid(row=0,column=4)

t2=Text(window,height=1,width=15)
t2.grid(row=1,column=3)
t5=Label(window,text="pounds")
t5.grid(row=1,column=4)

t3=Text(window,height=1,width=15)
t3.grid(row=2,column=3)
t6=Label(window,text="ounces")
t6.grid(row=2,column=4)


window.mainloop()


##Some Changes in design

# from tkinter import *
#
# window=Tk()
#
# def from_kg():
#     gram=float(e2_value.get())*1000
#     pound=float(e2_value.get())*2.20462
#     ounce=float(e2_value.get())*35.274
#     t1.delete("1.0", END)
#     t1.insert(END,gram)
#     t2.delete("1.0", END)
#     t2.insert(END,pound)
#     t3.delete("1.0", END)
#     t3.insert(END,ounce)
#
# e1=Label(window,text="Kg")
# e1.grid(row=0,column=0)
#
# e2_value=StringVar()
# e2=Entry(window,textvariable=e2_value)
# e2.grid(row=0,column=1)
#
# b1=Button(window,text="Convert",command=from_kg)
# b1.grid(row=0,column=2)
#
# t1=Text(window,height=1,width=20)
# t1.grid(row=1,column=0)
#
# t2=Text(window,height=1,width=20)
# t2.grid(row=1,column=1)
#
# t3=Text(window,height=1,width=20)
# t3.grid(row=1,column=2)
#
# window.mainloop()
