#!/usr/bin/env python3

import os
import sys
from gtts import gTTS
from playsound import playsound

def read_out_loud(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("speech.mp3")
    # Playing the converted file
    #os.system("start speech.mp3")
    playsound('speech.mp3')

mytext = sys.argv[1]
read_out_loud(mytext)
