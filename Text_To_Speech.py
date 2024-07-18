# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'charles owusu asare is a good boy to all kinds'
  
# Language we want to use 
language = 'en'
  

mytext = gTTS(text=mytext, lang=language, slow=False) 
  

mytext.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 

