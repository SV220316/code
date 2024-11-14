from gtts import gTTS
import tempfile
import os
import time
from playsound import playsound

def speak(text):
    # Create speech audio file
    tts = gTTS(text=text, lang='en-us', slow=False)
    timestamp = int(time.time())
    ResponseOP = os.path.join(tempfile.gettempdir(), f"response_{timestamp}.mp3")
    
    try:
        tts.save(ResponseOP)
    except Exception as e:
        print(f"Error saving TTS file: {e}")
        return

    # Play the MP3 file using playsound
    try:
        playsound(ResponseOP)  # Directly play the MP3
    except Exception as e:
        print(f"Error playing audio: {e}")
        return

def trial():
    speak("Hello! I am Prototype")

if __name__ == "__main__":
    trial()
