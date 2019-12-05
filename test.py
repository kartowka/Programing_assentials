from tkinter import *
from tkinter.ttk import Combobox

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Course Name:')
        self.lbl2=Label(win, text='Lecturer Name:')
        self.t1=Entry()
        self.t2=Entry()
        self.btn1 = Button(win, text='Submit')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=380, y=50)
        self.t2.place(x=485, y=50)
        self.data=("", "Exam", "Pre-Exam")
        self.cb=Combobox(win, values=self.data)
        self.cb.place(x=685, y=50)
        self.data1=("","1-Easy",'2','3','4','5','6',"7-Very Hard")
        self.cb2=Combobox(win,values=self.data1)
        self.cb2.place(x=885,y=50)
        self.data2=("", "Answer", "No-Answer")
        self.cb2=Combobox(win, values=self.data2)
        self.cb2.place(x=1085, y=50)
        self.btn1.place(x=1285,y=50)



        # self.b1=Button(win, text='Add', command=self.add)
        # self.b2=Button(win, text='Subtract')
        # self.b2.bind('<Button-1>', self.sub)
        # self.b1.place(x=100, y=150)
        # self.b2.place(x=200, y=150)
        # self.lbl3.place(x=100, y=200)
        # self.t3.place(x=200, y=200)
window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("1400x500+10+10")
window.mainloop()
