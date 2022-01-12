from gtts import gTTS

import os
import datetime
for filename in os.listdir(os.getcwd()+"/Articles/scripted"):
   with open(os.path.join(os.getcwd()+"/Articles/scripted", filename), 'r') as f: # open in readonly mode
    #   print(filename[:-4])
      print(f'Beginning recording {filename[:-4]}.mp3 {datetime.datetime.now()}')
      tts = gTTS(text=f.read(), lang='en', slow=True)
      tts.save('Outputs/scripted/'+filename[:-4]+'.mp3')
      print(f'Done recording recording {filename[:-4]}.mp3 {datetime.datetime.now()}')
