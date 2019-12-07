from tkinter import *
from tkinter.ttk import Combobox
import dataClasses as dC

class MyWindow:
    def __init__(self, win):
        self.courseName = StringVar()
        self.LecturerName = StringVar()
        self.lbl1=Label(win, text='Course Name:')
        self.lbl2=Label(win, text='Lecturer Name:')
        self.courseName=Entry(textvariable=self.courseName)
        self.LecturerName=Entry(textvariable=self.LecturerName)
        self.btn1 = Button(win, text='Submit',command=self.submit)
        self.lbl1.place(x=100, y=50)
        self.courseName.place(x=200, y=50)
        self.lbl2.place(x=380, y=50)
        self.LecturerName.place(x=485, y=50)
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
        self.searchResults=Label(win,text="Search Results: ")
        self.searchResults.place(x=100,y=150)
        self.listbox=Listbox(win)
        self.listbox.place(height=200,width=1185,x=100,y=200)
        

    def submit(self):
        print(self.courseName.get())
        print(self.LecturerName.get())




window=Tk()
mywin=MyWindow(window)
window.title('SCE Search Engine')
window.geometry("1400x500+10+10")
window.mainloop()
