from tkinter import *
from tkinter import messagebox,filedialog
from PIL import *
from pdf2image import convert_from_path


class UploadBox:
    def __init__(self,root):
        self.root=root
    def image_input(filename,path):
        #image save with specific name .jpg
        #add a picture with 3 parameters receive(imgPath,width-const)
        pages = convert_from_path(path, 500)
        i=1
        for page in pages:
            page.save('savedimages/'+filename+'_'+str(i)+'.jpg', 'JPEG')
            i+=1
        messagebox.showinfo("Messege","file upload complete!")
        return pages
