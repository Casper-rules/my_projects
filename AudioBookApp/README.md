# Creating audiobook out of  pdf file
The app is designed to allow user to choose a pdf file from the system and reads back the text content of the file.We use the google text to speech library to convert the text part of the file to an audio file. We save the audio file in an mp3 file. We use the playsound library to play the audio file saved.
following is the detailed description of the libraries used.
## PyPDF2:
PyPDF2 is an awesome pdf handeling library for python. We can use pip to install the liberary
``` 
pip install PyPDF2
```
We import PyPDF2 as pdf so that it's easier to use in the code and easy to write the code making it a littile cleaner and more readable.
We use the PdfFileReader function to read the pdf file. We open the file as read binary.The numPages is used to find the number of pages in the pdf file. We then use the getPage(page_index) to get particular page and to get the text vaalues in the file, we use extractText() function.
<br/>
## Tkinter :
Tkinter is used to provide a nice pop-up to provide the user an option to select the file they want to convert to the audiobook or to read it.<br/>
The program saves the audiobook and hence the user can listen to the book later if they want to.
Tkinter is used to ask users for the name of the mp3 file they want. This allows the user to have multiple audiobooks.
<br/>
## playsound:
Pure Python, cross platform, single function module with no dependencies for playing sounds.We us ethis library to play our mp3 audio book files ceated. The user is prompted if they want to play the file just after the conversion. If the user chooses to play, the playsound is used to play the audiobook. We can install the playsound using 
```
pip install playsound
```

## Google Text To Speech(gtts):
gTTS is a module and command line utility to save spoken text to mp3. It uses the Google Text to Speech (TTS) API. We import gTTS from gts. We can install the above module using
```
pip install gTTS
```
We set text to be converted to speech and the language we want it in and let it create the audio object. We then save the audio into an mp3 file. We ask the user to enter the name for the audio file.
