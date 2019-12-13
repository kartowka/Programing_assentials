from tkinter import *
from dataClasses import *
import searchdatabase
from pdf2img import *

class Question:
    def __init__(self,root):
        #window
        self.root=root
        self.root=Toplevel()
        self.root.title("Parliamentary Question")
        #Data of questinary
        Question.questionSubject=StringVar()
        Question.subQuestionSubject=StringVar()
        Question.numberOfParagraphs=StringVar()
        Question.difLvl=StringVar()
        Question.terms=StringVar()
        Question.year=StringVar()
        Question.semester=StringVar()
        Question.moed=StringVar()
        self.format=StringVar()
        #create widgets
        self.widgets()
    def openPdf2img(self):
        self.uploadfile=filedialog.askopenfilename()
    def submitToText(self):
        str=(self.questionSubject.get()+self.subQuestionSubject.get()+self.numberOfParagraphs.get()+self.difLvl.get()+self.terms.get()+self.year.get()+self.semester.get()+self.moed.get()+self.format.get())
        UploadBox.image_input(str,self.uploadfile)
        #add all to database.
        #searchdatabase.insert(self.questionSubject.get(),self.subQuestionSubject.get(),self.numberOfParagraphs.get(),self.difLvl.get(),self.terms.get(),self.year.get(),self.semester.get(),self.moed.get(),self.format.get())

    #drawing widgets
    def widgets(self):
        self.head=Label(self.root,text="Parliamentary Question",font=('',35),pady=10)
        self.head.pack()
        self.uploadfile=Button(self.root,text="Browse",font=('',25),pady=10,command=self.openPdf2img)
        self.uploadfile.pack()

        self.entryF=Frame(self.root,padx=10,pady=10)
        Label(self.entryF,text="Question subject",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.questionSubject,bd=5,font=('',9)).grid(row=0,column=1)
        Label(self.entryF,text="Sub question subject",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.subQuestionSubject,bd=5,font=('',9)).grid(row=1,column=1)
        Label(self.entryF,text="Number of paragraphs",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.numberOfParagraphs,bd=5,font=('',9)).grid(row=2,column=1)
        Label(self.entryF,text="Difficulty level(1-10)",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.difLvl,bd=5,font=('',9)).grid(row=3,column=1)
        Label(self.entryF,text="Mid/Final terms",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.terms,bd=5,font=('',9)).grid(row=4,column=1)
        Label(self.entryF,text="Year",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.year,bd=5,font=('',9)).grid(row=5,column=1)
        Label(self.entryF,text="Semester",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.semester,bd=5,font=('',9)).grid(row=6,column=1)
        Label(self.entryF,text="Moed",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=Question.moed,bd=5,font=('',9)).grid(row=7,column=1)
        Label(self.entryF,text="Question format",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.format,bd=5,font=('',9)).grid(row=8,column=1)
        Button(self.entryF,text="Submit Form",bd=4,font=("",15),padx=5,pady=5,command=self.submitToText).grid()
        self.entryF.pack()
