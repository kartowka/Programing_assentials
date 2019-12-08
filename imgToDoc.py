import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from docx.shared import Inches
from docx import Document
import docx

#FUNCTION TO CROP PDF TO DIFRENT PAGES

class UploadBox:
    def __init__(self,root):
        self.fileName=StringVar()
        self.label1=Label(root,text="please insert file with .png")
        self.fileNameInput=Entry(root)
        self.fileNameInput.insert(0,'please insert filename')
        self.fileNameInput.bind("<Button-1>",lambda event: self.clear_entry(event, self.fileNameInput))
        self.fileNameInput.place(x=120,y=30)
        self.label1.place(x=100, y=0)
        self.uploadTitle=Label(root,text="Upload png FILE")
        self.uploadBtn=Button(root,text='OPEN',command=self.image_input)
        self.uploadBtn.place(x=160,y=60)
        self.closeButton=Button(root,text="EXIT",command=self.close)
        self.closeButton.place(x=220,y=60)
    def clear_entry(self,event, entry):
        entry.delete(0, END)
    def image_input(self):
        #docs file create
        document = docx.Document()
        doc='.docx'
        fileName = filedialog.askopenfilename()
        #add a picture with 3 parameters receive(imgPath,width-const)
        document.add_picture(fileName, width=Inches(2.0))
        document.save("%s%s" %(self.fileNameInput.get(),doc))
        messagebox.showinfo("Messege","file upload complete!")
        return document
    def close(self):
        return window.destroy()
window=Tk()
mywin=UploadBox(window)
window.title('SCE - IMG2WORD')
window.geometry("400x200+10+10")
window.mainloop()
