from tkinter import *
from dataClasses import *

class main:
    def __init__(self,root):
        #window
        self.root=root
        #Data of questinary
        self.questionSubject=StringVar()
        self.subQuestionSubject=StringVar()
        self.numberOfParagraphs=StringVar()
        self.difLvl=StringVar()
        self.terms=StringVar()
        self.year=StringVar()
        self.semester=StringVar()
        self.moed=StringVar()
        self.format=StringVar()
        #A file
        self.newFile=open("test.txt","w+")
        #create widgets
        self.widgets()
    #saving all questinary into a text to send to database
    def submitToText(self):
        #newFile=open("1.txt","w")
        self.newFile.write(((self.questionSubject.get()+self.subQuestionSubject.get())+self.numberOfParagraphs.get()+self.difLvl.get()+self.terms.get()+self.year.get()+self.semester.get()+self.moed.get()+self.format.get()))
         

    #drawing widgets
    def widgets(self):
        self.head=Label(self.root,text="Parliamentary Question",font=('',35),pady=10)        
        self.head.pack()
        self.entryF=Frame(self.root,padx=10,pady=10)
        Label(self.entryF,text="Question subject",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.questionSubject,bd=5,font=('',9)).grid(row=0,column=1)
        Label(self.entryF,text="Sub question subject",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.subQuestionSubject,bd=5,font=('',9)).grid(row=1,column=1)
        Label(self.entryF,text="Number of paragraphs",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.numberOfParagraphs,bd=5,font=('',9)).grid(row=2,column=1)
        Label(self.entryF,text="Difficulty level(1-10)",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.difLvl,bd=5,font=('',9)).grid(row=3,column=1)
        Label(self.entryF,text="Mid/Final terms",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.terms,bd=5,font=('',9)).grid(row=4,column=1)
        Label(self.entryF,text="Year",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.year,bd=5,font=('',9)).grid(row=5,column=1)
        Label(self.entryF,text="Semester",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.semester,bd=5,font=('',9)).grid(row=6,column=1)
        Label(self.entryF,text="Moed",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.moed,bd=5,font=('',9)).grid(row=7,column=1)
        Label(self.entryF,text="Question format",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.format,bd=5,font=('',9)).grid(row=8,column=1)
        Button(self.entryF,text="Submit Form",bd=4,font=("",15),padx=5,pady=5,command=self.submitToText).grid()
        self.entryF.pack()

#creating window application
root=Tk()
root.title("Parliamentary Question")
main(root)
root.mainloop()

