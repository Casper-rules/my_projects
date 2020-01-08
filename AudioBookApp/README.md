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
Tkinter is used to provide a nice pop-up to provide the user an option to select the file they want to convert to the audiobook or to read it.
The program 
