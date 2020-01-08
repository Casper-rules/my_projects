import PyPDF2 as pdf
from playsound import playsound
from gtts import gTTS
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filelocation=askopenfilename()
_file= open(filelocation,'rb')
pdf_file=pdf.PdfFileReader(_file)

_string=''
for pageNumber in range(pdf_file.numPages):
    page=pdf_file.getPage(pageNumber)
    extractedText=page.extractText()
    if extractedText:
        _string+=extractedText
convertAudio=gTTS(text=_string,lang='en')
convertAudio.save('book.mp3')
playsound('book.mp3')
    
_file.close()