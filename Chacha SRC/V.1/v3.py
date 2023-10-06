import aiml
import speech_recognition as sr
import pyttsx3
import langid
import threading
import logging

logging.basicConfig(filename='chatbot.log', level=logging.INFO,format='%(message)s')

english_kernel = aiml.Kernel()
hindi_kernel = aiml.Kernel()

english_kernel.learn("English.aiml")
hindi_kernel.learn("Hindi.aiml")


recognizer = sr.Recognizer()


engine_english = pyttsx3.init()
engine_hindi = pyttsx3.init()


def speak(text, language="en"):
    if language == "en":
        engine_english.say(text)
    elif language == "hi":
        engine_hindi.say(text)
    engine_english.runAndWait()


def handle_voice_input():
    introduction = "Hello, I am Chacha Chaudhary. How can I assist you today?"
    speak(introduction, language="hi")

    while True:
        user_input = get_spoken_input()

        if user_input == "exit":
            print("Chacha Chaudhary: Goodbye!")
            break

        detected_language, _ = langid.classify(user_input)

        if "chacha chaudhary" in user_input.lower():
            response = "Yes, I am Chacha Chaudhary. How can I assist you?"
            speak(response, detected_language)
            continue

        respond_to_user_input(user_input, detected_language)  


def handle_typed_input():
    introduction = "Hello, I am Chacha Chaudhary. How can I assist you today?"
    print(introduction)

    while True:
        user_input = get_typed_input()

        if user_input == "exit":
            print("Chacha Chaudhary: Goodbye!")
            break

        detected_language, _ = langid.classify(user_input)

        if "chacha chaudhary" in user_input.lower():
            response = "Yes, I am Chacha Chaudhary. How can I assist you?"
            print(response)
            continue

        respond_to_user_input(user_input, detected_language)  


def respond_to_user_input(user_input, detected_language):
    if detected_language == "hi":
        response = hindi_kernel.respond(user_input)
    else:
        response = english_kernel.respond(user_input)

    if response:
        print(f"Chacha Chaudhary ({detected_language}):", response)
        speak(response, detected_language)
    else:
        print(f"Chacha Chaudhary ({detected_language}): I'm sorry, I couldn't understand your request.")


def get_spoken_input():
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


def get_typed_input():
    user_input = input("You (Type): ").lower()
    return user_input

if __name__ == "__main__":
    while True:
        print("\nSelect Input Mode:")
        print("1. Voice Input")
        print("2. Type Input")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            handle_voice_input()
        elif choice == "2":
            handle_typed_input()
        elif choice == "3":
            print("Chacha Chaudhary: Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
