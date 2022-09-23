# importing the modules
import PyPDF2
import pyttsx3
import pdfplumber

file = 'file.pdf'

# Create a PDF file Object
pdfFileObj = open(file, 'rb')

# Create a PDF file Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Get the number of pages
pages = pdfReader.numPages

# Create a plumber object and loop through all pages
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = pages.extract_text()
        print(text)

        # reading the text
        speak = pyttsx3.init()
        speak.say(text)
        speak.runAndWait()


