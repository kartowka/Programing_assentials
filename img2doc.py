import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from docx.shared import Inches
from docx import Document
import docx
import logging

logging.basicConfig(filename="log.log",filemode='a+',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
logger.info("img2doc.py run as expected.")


#FUNCTION TO CROP PDF TO DIFRENT PAGES

class img2document:
    def __init__(self,root):
        self.root=root
        self.root=Toplevel()
        self.root.title("Img 2 Document")
        self.root.geometry('700x500')
        self.fileNameInput=StringVar()
        self.widgets()
    def widgets(self):
        self.head=Label(self.root,text="Image 2 Document",font=('',35),pady=10)
        self.head.pack()

        self.entryF=Frame(self.root,padx=10,pady=10)
        Label(self.entryF,text="Enter filename",font=("",20),pady=3,padx=3).grid(sticky=W)
        Entry(self.entryF,textvariable=self.fileNameInput,bd=5,font=('',9)).grid(row=0,column=1)
        Button(self.entryF,text="Browse",bd=4,font=("",15),padx=5,pady=5,command=self.image_input).grid(row=1,column=0)
        Button(self.entryF,text="Exit",bd=4,font=("",15),padx=5,pady=5,command=self.close).grid(row=1,column=1)
        self.entryF.pack()


    def clear_entry(self,event, entry):
        entry.delete(0, END)
    def image_input(self):
        """function of img2pdf - convert the img to pdf format"""
        #docs file create
        answer=True
        document = docx.Document()
        doc='.docx'
        #add a picture with 3 parameters receive(imgPath,width-const)
        while(answer==True):
            fileName = filedialog.askopenfilename()
            answer=messagebox.askyesno("Question","Do you want to add more files?")
            if(fileName==()):
                return
            document.add_picture(fileName, width=Inches(6.0),height=Inches(1.85))
            messagebox.showinfo("Messege","file upload complete!")
            logger.info("file upload complete.")
        if(answer==False):
            document.save('savedocs/'+"%s%s" %(self.fileNameInput.get(),doc))
            messagebox.showinfo("Messege","document file created!")
            logger.info("file created.")

        self.close()
    def close(self):
        return self.root.destroy()
