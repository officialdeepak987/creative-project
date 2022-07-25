from PyPDF2 import PdfReader
import pyttsx3 
import PyPDF2
book =open('shell scripting book.pdf','rb')
PdfReader=PyPDF2.PdfFileReader(book)
pages =PdfReader.numPages
print(pages)
speaker =pyttsx3.init()
for num in range(7,pages):
   pages =PdfReader.getPage(8)
text=pages.extractText()

speaker.say(text)
speaker.runAndWait()
