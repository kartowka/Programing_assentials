import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path
#FUNCTION TO CROP PDF TO DIFRENT PAGES

class UploadBox:
    def __init__(self,root):
        self.fileName=StringVar()
        self.label1=Label(root,text="please insert file with .pdf")
        self.fileNameInput=Entry(root)
        self.fileNameInput.insert(0,'please insert filename')
        self.fileNameInput.bind("<Button-1>",lambda event: self.clear_entry(event, self.fileNameInput))
        self.fileNameInput.place(x=120,y=30)
        self.label1.place(x=100, y=0)
        self.uploadTitle=Label(root,text="Upload PDF FILE")
        self.uploadBtn=Button(root,text='OPEN',command=self.CropFile)
        self.uploadBtn.place(x=160,y=60)
        self.closeButton=Button(root,text="EXIT",command=self.close)
        self.closeButton.place(x=220,y=60)
    def clear_entry(self,event, entry):
        entry.delete(0, END)
    def CropFile(self):
        self.filename = filedialog.askopenfilename()
        #OPENING FILE
        self.inputPDF=PdfFileReader(self.filename,'rb')
        #GETTING NUMBER OF PAGES
        self.pageNumber=self.inputPDF.getNumPages()
        #LOOP TO RUN AND CROP NUM OF PAGES
        for i in range(self.pageNumber):
            output = PdfFileWriter()
            output.addPage(self.inputPDF.getPage(i))
            with open(self.fileNameInput.get()+'%s.pdf' % i, "wb") as outputStream:
                 output.write(outputStream)
    def close(self):
        return window.destroy()
window=Tk()
mywin=UploadBox(window)
window.title('SCE - PDF FILE2PAGE')
window.geometry("400x200+10+10")
window.mainloop()
