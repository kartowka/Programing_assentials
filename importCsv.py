from tkinter import *
import csv
import searchdatabase
from tkinter import filedialog
from tkinter import messagebox


class ImportCSV:
    def __init__(self,root):
        self.root=root
        self.root=Toplevel()
        self.root.title("CSV File Import")
        self.root.geometry('700x500')
        self.fileNameInput=""
        self.widgets()
    def widgets(self):
        self.head=Label(self.root,text="CSV File Import",font=('',35),pady=10)
        self.head.pack()
        self.uploadfile=Button(self.root,text="Browse",bd=4,font=("",15),padx=5,pady=5,command=self.filePath)
        self.uploadfile.pack()


        self.entryF=Frame(self.root,padx=10,pady=10)
        Button(self.entryF,text="Ok",bd=4,font=("",15),padx=5,pady=5,command=self.importc).grid(row=1,column=0)
        Button(self.entryF,text="Exit",bd=4,font=("",15),padx=5,pady=5,command=self.close).grid(row=1,column=1)
        self.entryF.pack()
    def filePath(self):
        self.fileName=filedialog.askopenfilename()
        self.fileNameInput=self.fileName
        return self.fileName
    def importc(self):
        #OPENING FILE
        ifile  = open(self.fileNameInput, "r")
        if ifile==None:
            return
        read = csv.reader(ifile)
        for row in read :
            searchdatabase.insertFromCSV(row)
        #importCsv_backend.insert(to_db)
        messagebox.showinfo("Messege","file upload complete!")
        self.close()
    def close(self):
        return self.root.destroy()
