from docx.shared import Inches
from docx import Document
import docx

#function to input image to word document
def image_input(docName,imgPath,size=2):
    #docs file create
    document = docx.Document()
    #add a picture with 3 parameters receive(imgPath,width-const)
    document.add_picture(imgPath, width=Inches(2.0))
    document.save(docName)
    return document

#MUST INPUT DOC NAME WITH ENDING .DOCX
#IMAGE PATH MUST END WITH .PNG
