
#Built by @AnatuGreen on 28-29/09/2022
#We can also consider using https://www.wordsapi.com/

from pathlib import Path
from tkinter import ttk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import END, Frame, Label, Tk, Canvas, Entry, Text, Button, PhotoImage

#Import dictionary for this app
from PyDictionary import PyDictionary as Dictionary

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("390x750")
window.configure(bg = "#FFFFFF")
window.title("Py English Dictionary By @AnatuTech")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    195.0,
    422.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    175.0,
    50.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    168.5,
    50,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0,
    justify='center', font=('Times', 15,'bold')
)
entry_1.place(
    x=47.5,
    y=24.0,
    width=242.0,
    height=51.0
)

def defineFunc():
    enteredText = entry_1.get()
    enteredText=enteredText.upper()
    meanng=Dictionary.meaning(enteredText)
    #print(meanng)
    #Configure the meaning label that will be seen below. It originally has empty string so let us give it some text
    definitionn.delete('1.0','end')#Delete the previous text there
    if meanng:
        definitionn.insert(1.0,meanng) #Insert the word meaning at the end of the
    else:
        definitionn.insert(1.0,f"No meaning of the word {enteredText} was found on dictionary.com")

#Synonyms finder
def synonymFunc():
    enteredText = entry_1.get()
    enteredText=enteredText.upper()
    synonym=Dictionary.synonym(enteredText)
    #print(synonym)
    definitionn.delete('1.0','end')#Delete the previous text there
    if synonym:
        definitionn.insert(1.0,synonym) #Insert the word meaning at the end of the
    else:
        definitionn.insert(1.0,f"No synonyms of the word {enteredText} was found on dictionary.com")

#Antonyms finder function
def antonymFunc():
    enteredText = entry_1.get()
    enteredText=enteredText.upper()
    antonym=Dictionary.antonym(enteredText)
    #print(antonym)
    definitionn.delete('1.0','end')#Delete the previous text there
    if antonym:
        definitionn.insert(1.0,antonym) #Insert the word meaning at the end of the
    else:
        definitionn.insert(1.0,f"No antonyms of the word {enteredText} was found on dictionary.com")



#The search botton
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=defineFunc,
    relief="flat"
)
button_1.place(
    x=326.0,
    y=31.0,
    width=45.0,
    height=39.0
)

#The synonyms button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=synonymFunc,
    relief="flat"
)
button_2.place(
    x=42.0,
    y=668.0,
    width=63.0,
    height=63.0
)
#End of synonyms button

#The antonyms button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=antonymFunc,
    relief="flat"
)
button_3.place(
    x=163.0,
    y=668.0,
    width=63.0,
    height=63.0
)
#End of antonyms button

#Reacd text out loud
def text2Speech():
    enteredText = entry_1.get()
    enteredText=enteredText.upper()
    meaning=Dictionary.meaning(enteredText)
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(meaning)
    engine.runAndWait()

#The Read Out button
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=text2Speech,
    relief="flat"
)
button_4.place(
    x=284.0,
    y=668.0,
    width=63.0,
    height=63.0
)
#End of Read Out button

#Frame to contain the meaning has to be scrollable
meaningFrame = Frame(window, height=250, width=200,)
definitionn = Text(meaningFrame, width=200, height=250, bg="white", font=('Times', 13,), wrap='word', relief=None)
definitionn.pack(padx=20, pady=5)
meaningFrame.pack(pady=110)

#Make sure the text is scrollable vertically in case the text is too long
vertScroll = ttk.Scrollbar(meaningFrame, orient='vertical', command=definitionn.yview)

window.resizable(False, False)
window.mainloop()
