import pyttsx3
import PyPDF2

book = open('arthas.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
# for num in range(8, pages):
page = pdfReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
