import speech_recognition as sr
import langid

def get_spoken_input(recognizer, language_choice):
    with sr.Microphone() as source:
        print("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            if language_choice == "hi":
                user_input = recognizer.recognize_google(audio, language="hi-IN")
            else:
                user_input = recognizer.recognize_google(audio, language="en-US")
            print(f"You ({language_choice.capitalize()} Voice):", user_input)
            return user_input.lower(), language_choice
        except sr.WaitTimeoutError:
            print("Chacha Chaudhary: You didn't provide any input. Goodbye.")
            return "", language_choice
        except sr.UnknownValueError:
            print("Chacha Chaudhary: I couldn't understand your voice. Please try again.")
            return "", language_choice
        except sr.RequestError as e:
            print(f"Chacha Chaudhary: Error with speech recognition: {e}")
            return "", language_choice

def detect_input_language(user_input):
    detected_language, _ = langid.classify(user_input)
    return detected_language
