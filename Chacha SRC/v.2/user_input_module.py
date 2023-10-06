import speech_recognition as sr
import langid

def get_spoken_input(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            user_input = recognizer.recognize_google(audio, language="hi-IN")
            print("You (Voice):", user_input)
            return user_input.lower()
        except sr.WaitTimeoutError:
            print("Chacha Chaudhary: You didn't provide any input. Goodbye.")
            return ""
        except sr.UnknownValueError:
            print("Chacha Chaudhary: I couldn't understand your voice. Please try again.")
            return ""
        except sr.RequestError as e:
            print(f"Chacha Chaudhary: Error with speech recognition: {e}")
            return ""

def detect_input_language(user_input):
    detected_language, _ = langid.classify(user_input)
    return detected_language
