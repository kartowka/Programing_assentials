from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path

reader=PdfFileReader('C:/Users/PROPHET/Downloads/Python_HW1 (1).pdf','r ')
def CropFile(FilePath,PageNumber,x,y,h,w):
    reader=PdfFileReader(FilePath,'r')
    page=reader.getPage(PageNumber)
    page.cropBox.getUpperRight()
    page.cropBox.getUpperLeft()
    page.cropBox.getLowerRight()
    page.cropBox.getLowerLeft()
    return reader

reader=CropFile('C:/Users/PROPHET/Downloads/Python_HW1 (1).pdf',1,7,3,5,5)
page=convert_from_path('reader',400)
page[0].save("reader")