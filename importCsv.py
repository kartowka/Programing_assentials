from tkinter import *
import csv
import searchdatabase
from tkinter import filedialog
from tkinter import messagebox


class UploadBox:
    def __init__(self,root):
        self.fileNameInput=Entry(root,width=80)
        self.fileNameInput.insert(0,'')
        #self.fileNameInput.bind("<Button-1>",lambda event: self.clear_entry(event, self.fileNameInput))
        self.fileNameInput.place(x=120,y=50)
        self.uploadBtn=Button(root,text='Browse',command=self.filePath)
        self.uploadBtn.place(x=800,y=30)
        self.closeButton=Button(root,text="EXIT",command=self.close)
        self.closeButton.place(x=160,y=80)
        self.okButton=Button(root,text="Ok",command=self.importc)
        self.okButton.place(x=120,y=80)
    def clear_entry(self,event, entry):
        entry.delete(0, END)
    def filePath(self):
        self.fileName=filedialog.askopenfilename()
        self.fileNameInput.insert(0,self.fileName)
        return self.fileName
    def importc(self):
        #OPENING FILE
        ifile  = open(self.fileNameInput.get(), "r")
        read = csv.reader(ifile)
        for row in read :
            searchdatabase.insertFromCSV(row)
        #importCsv_backend.insert(to_db)
        messagebox.showinfo("Messege","file upload complete!")
    def close(self):
        return window.destroy()
window=Tk()
mywin=UploadBox(window)
window.title('SCE - import CSV file')
window.geometry("1000x200+10+10")
window.mainloop()
