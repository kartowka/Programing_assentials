from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path

def CropFile(FilePath):
    inputPDF=PdfFileReader(FilePath,'rb')
    pageNumber=inputPDF.getNumPages()
    for i in range(pageNumber):
        output = PdfFileWriter()
        output.addPage(inputPDF.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
             output.write(outputStream)
