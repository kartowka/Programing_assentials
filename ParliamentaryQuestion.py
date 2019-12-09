from tkinter import *
from dataClasses import *

root = Tk()
theLabel=Label(root,text="Parliamentary Question",bg="black",fg="white")
#theLabel.pack(fill=X)
Label_1=Label(root,text="question subject")
Label_2=Label(root,text="sub question subject")
Label_3=Label(root,text="difficulty level(1-10)")
Label_4=Label(root,text="mid terms/final term")
Label_5=Label(root,text="year")
Label_6=Label(root,text="semester")
Label_7=Label(root,text="Moed")
Label_8=Label(root,text="question format")
entry_1=Entry(root)
entry_2=Entry(root)
entry_3=Entry(root)
entry_4=Entry(root)
entry_5=Entry(root)
entry_6=Entry(root)
entry_7=Entry(root)
entry_8=Entry(root)

Label_1.grid(row=0)
Label_2.grid(row=1)
Label_3.grid(row=2)
Label_4.grid(row=3)
Label_5.grid(row=4)
Label_6.grid(row=5)
Label_7.grid(row=6)
Label_8.grid(row=7)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1)
entry_4.grid(row=3,column=1)
entry_5.grid(row=4,column=1)
entry_6.grid(row=5,column=1)
entry_7.grid(row=6,column=1)
entry_8.grid(row=7,column=1)

submitButton=Button(root, text="submit" )
submitButton.pack()


root.mainloop()

