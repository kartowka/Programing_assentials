from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Combobox
import backend
import searchdatabase
import os
from rating import Rating
import subprocess
import webbrowser

class Student:
    def __init__(self,window):
        self.window = window
        #self.window = Toplevel()
        self.window.geometry('1400x600')
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.frame = Frame(self.window,width=1400, height=200, pady=3)
        self.questionSubject = StringVar()
        self.subQuestionSubject = StringVar()
        self.year=StringVar()
        self.difLvl=("1",'2','3','4','5','6',"7","8","9","10")
        self.terms=("Pre-Exam","Exam")
        self.semester=("first","second","third")
        self.moed=("first","second")
        self.format=("pdf","word")

        Label(self.frame,text="Question subject: ",font=("",14),pady=3,padx=3).place(x=10,y=50)
        Entry(self.frame,textvariable=self.questionSubject,font=("",14),width=14).place(x=185,y=50)

        Label(self.frame,text="sub question subject: ",font=("",14),pady=3,padx=3).place(x=370,y=50)
        Entry(self.frame,textvariable=self.subQuestionSubject,font=("",14),width=14).place(x=590,y=50)

        Label(self.frame,text="Difficulty: ",font=("",14),pady=3,padx=3).place(x=800,y=50)
        self.dif_combo=Combobox(self.frame,values=self.difLvl,font=("",14),width=5)
        self.dif_combo.place(x=900,y=50)

        Label(self.frame,text="Term: ",font=("",14),pady=3,padx=3).place(x=120,y=100)
        self.terms_combo=Combobox(self.frame,values=self.terms,font=("",14),width=8)
        self.terms_combo.place(x=185,y=100)

        Label(self.frame,text="Year: ",font=("",14),pady=3,padx=3).place(x=300,y=100)
        Entry(self.frame,textvariable=self.year,font=("",14),width=6).place(x=360,y=100)

        Label(self.frame,text="Semester: ",font=("",14),pady=3,padx=3).place(x=430,y=100)
        self.semester_combo=Combobox(self.frame,values=self.semester,font=("",14),width=8)
        self.semester_combo.place(x=530,y=100)

        Label(self.frame,text="Moed: ",font=("",14),pady=3,padx=3).place(x=640,y=100)
        self.moed_combo=Combobox(self.frame,values=self.moed,font=("",14),width=5)
        self.moed_combo.place(x=700,y=100)

        Label(self.frame,text="Format: ",font=("",14),pady=3,padx=3).place(x=780,y=100)
        self.format_combo=Combobox(self.frame,values=self.format,font=("",14),width=5)
        self.format_combo.place(x=860,y=100)

        Button(self.frame, text="Submit",bd=4,font=("",14),padx=3,pady=3,command=self.submit).place(x=950,y=100)
        self.frame.pack(side=TOP)

        self.cnt_frame = Frame(self.window, width=1400, height=400)
        Label(self.cnt_frame,text="Search Results: ",font=("",14),pady=3,padx=3).place(x=10,y=0)
        self.search_result=Listbox(self.cnt_frame,font=("",14))
        self.search_result.place(height=300,width=1050,x=10,y=40)
        Button(self.cnt_frame, text="Download Selected",bd=4,font=("",14),padx=3,pady=3,command=self.downloadFile).place(x=160,y=0)
        Button(self.cnt_frame, text="Rating",bd=4,font=("",14),padx=3,pady=3,command=self.rating).place(x=950,y=0)
        self.cnt_frame.pack(side=TOP)




        # self.listbox=Listbox(self.window)
        # self.listbox.place(height=200,width=1185,x=100,y=200)

    def submit(self):
        self.search_result.delete(0,END)
        for row in searchdatabase.search(self.questionSubject.get(),self.subQuestionSubject.get(),self.dif_combo.get(),self.terms_combo.get(),self.year.get(),self.semester_combo.get(),self.moed_combo.get(),self.format_combo.get()):
            self.search_result.insert(END,row)

    #returns filename from database .pdf or docx
    def tup2str(self,tup):
        str=''.join(tup[1:-1])
        ends=''.join(tup[-1])
        if ends=='word':
            ends='docx'
        str=str+'.'+ends
        return str

    def rating(self):
        selected_tuple=self.search_result.curselection()
        if selected_tuple==():
            return
        value = self.search_result.get(selected_tuple)
        #self.window.destroy()
        obj=Rating(self.window,value)


    def downloadFile(self):
        selected_tuple=self.search_result.curselection()
        if selected_tuple==():
            return
        value = self.search_result.get(selected_tuple)
        file='savedocs/'+self.tup2str(value)
        #path_to_krop = '/snap/bin/krop.krop-app'
        if(os.path.exists(file)):
            #webbrowser.open(file)
            webbrowser.get(using='google-chrome').open(file)

            #subprocess.call([path_to_krop, file])
        else:
            messagebox.showinfo('Messege','file not found.')
            return
