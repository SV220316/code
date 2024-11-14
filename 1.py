from gtts import gTTS
import simpleaudio as sa
import tempfile
import os
import time
from pydub import AudioSegment

def speak(text):
    # Create the speech audio file
    tts = gTTS(text=text, lang='en-us', slow=False)
    timestamp = int(time.time())
    ResponseOP = os.path.join(tempfile.gettempdir(), f"response_{timestamp}.mp3")
    try:
        tts.save(ResponseOP)
    except Exception as e:
        print(f"Error saving TTS file: {e}")
        return

    # Convert MP3 to WAV
    try:
        sound = AudioSegment.from_mp3(ResponseOP)
        wav_response = os.path.join(tempfile.gettempdir(), f"response_{timestamp}.wav")
        sound.export(wav_response, format="wav")
    except Exception as e:
        print(f"Error converting MP3 to WAV: {e}")
        return

    # Play the WAV file using simpleaudio
    try:
        wave_obj = sa.WaveObject.from_wave_file(wav_response)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(f"Error playing audio: {e}")
        return

def trial():
    speak("Hello! I am Prototype")

if __name__ == "__main__":
    trial()
