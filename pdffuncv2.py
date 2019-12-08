import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path
#FUNCTION TO CROP PDF TO DIFRENT PAGES

class UploadBox:
    def __init__(self,root):
        self.fileName=StringVar()
        self.label1=Label(root,text="filename")
        self.fileNameInput1=Entry(root,width=80)
        self.fileNameInput1.insert(0,'enter filename')
        self.fileNameInput1.bind("<Button-1>",lambda event: self.clear_entry(event, self.fileNameInput1))
        self.fileNameInput1.place(x=120,y=30)
        self.fileNameInput=Entry(root,width=80)
        self.fileNameInput.insert(0,'')
        #self.fileNameInput.bind("<Button-1>",lambda event: self.clear_entry(event, self.fileNameInput))
        self.fileNameInput.place(x=120,y=50)
        self.label1.place(x=120, y=0)
        self.uploadBtn=Button(root,text='Browse',command=self.filePath)
        self.uploadBtn.place(x=800,y=30)
        self.closeButton=Button(root,text="EXIT",command=self.close)
        self.closeButton.place(x=160,y=80)
        self.okButton=Button(root,text="Ok",command=self.CropFile)
        self.okButton.place(x=120,y=80)
    def clear_entry(self,event, entry):
        entry.delete(0, END)
    def filePath(self):
        self.fileName=filedialog.askopenfilename()
        self.fileNameInput.insert(0,self.fileName)
        return self.fileName
    def CropFile(self):
        #self.filename = filedialog.askopenfilename()
        #OPENING FILE
        self.inputPDF=PdfFileReader(self.fileNameInput.get(),'rb')
        #GETTING NUMBER OF PAGES
        self.pageNumber=self.inputPDF.getNumPages()
        #LOOP TO RUN AND CROP NUM OF PAGES
        for i in range(self.pageNumber):
            output = PdfFileWriter()
            output.addPage(self.inputPDF.getPage(i))
            with open(self.fileNameInput1.get()+'%s.pdf' % i, "wb") as outputStream:
                 output.write(outputStream)
        messagebox.showinfo("Messege","file upload complete!")
    def close(self):
        return window.destroy()
window=Tk()
mywin=UploadBox(window)
window.title('SCE - PDF FILE2PAGE')
window.geometry("1000x200+10+10")
window.mainloop()
