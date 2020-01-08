import PyPDF2 as pdf
from playsound import playsound
from gtts import gTTS
from tkinter import Tk,simpledialog,ttk
from tkinter.filedialog import askopenfilename

def play():
    audioFile=askopenfilename()
    playsound(audioFile)

def _exit():
    _file.colse()
    exit()

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
audioBookName=simpledialog.askstring(title='fileName',prompt='Enter a filename : ')
convertAudio.save(audioBookName+'.mp3')
popUp=Tk()
popUp.wm_title('Play?')
label=ttk.Label(popUp,text="do you want to play the audiofile now?")
label.pack(side="top", fill="x", pady=10)
B1 = ttk.Button(popUp, text="No, Exit", command = _exit)
B2 = ttk.Button(popUp,text="|> Play",command=play)
B2.grid()
B1.pack()
popUp.mainloop()