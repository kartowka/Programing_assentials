from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path
#FUNCTION TO CROP PDF TO DIFRENT PAGES
def CropFile(FilePath):
    #OPENING FILE
    inputPDF=PdfFileReader(FilePath,'rb')
    #GETTING NUMBER OF PAGES
    pageNumber=inputPDF.getNumPages()
    #LOOP TO RUN AND CROP NUM OF PAGES
    for i in range(pageNumber):
        output = PdfFileWriter()
        output.addPage(inputPDF.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
             output.write(outputStream)
