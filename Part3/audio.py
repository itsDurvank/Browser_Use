import pyttsx3
tts = pyttsx3.init()
tts.setProperty('rate', 150)
def speak(text):
        """Speak text using TTS"""
        print(f"🎤 Speaking: {text}")
        tts.say(text)
        tts.runAndWait()



