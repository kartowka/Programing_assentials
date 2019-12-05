from PyPDF2 import PdfFileReader,PdfFileWriter

reader=PdfFileReader('C:/Users/PROPHET/Downloads/Python_HW1 (1).pdf','r ')
page=reader.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())
print(page.cropBox.getLowerRight())

print("hrllo patrick")