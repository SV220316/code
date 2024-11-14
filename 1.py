import sounddevice as sd
import numpy as np
from gtts import gTTS
import tempfile
import os
import time
from scipy.io.wavfile import write
from pydub import AudioSegment

def speak(text):
    # Generate speech using gTTS
    tts = gTTS(text=text, lang='en-us', slow=False)
    timestamp = int(time.time())
    mp3_path = os.path.join(tempfile.gettempdir(), f"response_{timestamp}.mp3")
    
    try:
        tts.save(mp3_path)
    except Exception as e:
        print(f"Error saving TTS file: {e}")
        return

    # Convert MP3 to WAV using pydub
    sound = AudioSegment.from_mp3(mp3_path)
    wav_path = os.path.join(tempfile.gettempdir(), f"response_{timestamp}.wav")
    sound.export(wav_path, format="wav")
    
    # Read the WAV file and play using sounddevice
    try:
        fs, data = write(wav_path, np.array(sound.get_array_of_samples()))
        sd.play(data, fs)  # Play the WAV file
        sd.wait()  # Wait for the sound to finish
    except Exception as e:
        print(f"Error playing WAV: {e}")
        return

def trial():
    speak("Hello! I am Prototype")

if __name__ == "__main__":
    trial()
