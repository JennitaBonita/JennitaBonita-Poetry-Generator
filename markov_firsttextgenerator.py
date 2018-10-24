# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:46 2018

@author: gjenni4
"""

import markovify

with open ("use.txt") as textfile:
    author = textfile.read()
    
with open ("second.txt") as textfile:
    second = textfile.read()

    
author_model = markovify.Text(author)
second_model = markovify.Text(second)

synthesized_model = markovify.combine([author_model, second_model], [1,1])

#
# print five randomly-generated sentences
for i in range(3):
    poem = synthesized_model.make_sentence()


    
    # import libraries
from playsound import playsound
from gtts import gTTS

# text to speech
tts = gTTS(text=poem, lang='en')

# write audio file
tts.save("poem.mp3")

# play audio file
playsound("poem.mp3")