from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import *
from pdf2image import convert_from_path


class UploadBox:
    def __init__(self,root):
        self.fileName=StringVar()
        self.label1=Label(root,text="please insert pdf file")
        self.fileNameInput=Entry(root)
        self.fileNameInput.insert(0,'please insert filename')
        self.fileNameInput.bind("<Button-1>",lambda event: self.clear_entry(event, self.fileNameInput))
        self.fileNameInput.place(x=120,y=30)
        self.label1.place(x=100, y=0)
        self.uploadTitle=Label(root,text="Upload pdf FILE")
        self.uploadBtn=Button(root,text='OPEN',command=self.image_input)
        self.uploadBtn.place(x=160,y=60)
        self.closeButton=Button(root,text="EXIT",command=self.close)
        self.closeButton.place(x=220,y=60)
    def clear_entry(self,event, entry):
        entry.delete(0, END)
    def image_input(self):
        #docs file create
        #add a picture with 3 parameters receive(imgPath,width-const)
        fileName = filedialog.askopenfilename()
        pages = convert_from_path(fileName, 500)
        i=1
        for page in pages:
            page.save(self.fileNameInput.get()+str(i)+'.jpg', 'JPEG')
            i+=1
        messagebox.showinfo("Messege","file upload complete!")
        return pages
    def close(self):
        return window.destroy()
window=Tk()
mywin=UploadBox(window)
window.title('SCE - pdf2image')
window.geometry("400x200+10+10")
window.mainloop()
