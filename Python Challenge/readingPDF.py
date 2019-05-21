# importing all the required modules
import PyPDF2

# creating an object
file = open('mess.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
a = PyPDF2.extractText()
print(fileReader.numPages)
