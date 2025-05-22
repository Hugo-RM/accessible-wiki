import os
from gtts import gTTS

language = "en"

# A simple function to create the audio files using the name and its text
def convertText(title, myText):

    filename = f"{title}.mp3"
    filepath = os.path.join("static", filename)

    # If the audio file already exists, the function will end to improve runtime
    if os.path.exists(filepath):
        return
        
    myobj = gTTS(text=myText, lang=language, slow=False)
    myobj.save(f"static/{filename}")
